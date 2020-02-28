import datetime as dt

import numpy as np
import numpy.testing as npt
import pytest
from scmdata import ScmDataFrame

import test_scm


def test_get_datastore_unallocated_array_error():
    tdstore = test_scm.Datatypes.datastore()
    with pytest.raises(ValueError):
        tdstore.magnitude

def test_set_datastore_unallocated_array_error():
    tdstore = test_scm.Datatypes.datastore()
    with pytest.raises(ValueError):
        tdstore.magnitude = np.arange(4)

def test_get_datastore_allocated_array():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4, "dimensionless")
    assert isinstance(tdstore.magnitude, np.ndarray)

def test_set_datastore_allocated_array():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4, "dimensionless")
    tdstore.magnitude = np.arange(4)
    npt.assert_array_equal(tdstore.magnitude, np.arange(4))

def test_get_datastore_unit():
    tdstore = test_scm.Datatypes.datastore()
    assert tdstore.unit == b""

def test_set_datastore_unit():
    tdstore = test_scm.Datatypes.datastore()
    assert tdstore.unit == b""
    tdstore.unit = "Gt CO2"
    assert tdstore.unit == b"Gt CO2".ljust(1024)

def test_set_datastore():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4, "dimensionless")
    test_scm.library.set_datastore(tdstore, np.arange(4), "K")
    npt.assert_array_equal(tdstore.magnitude, np.arange(4))
    assert tdstore.unit == b"K".ljust(1024)

def test_set_datastore_wrong_size():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4, "dimensionless")
    test_scm.library.set_datastore(tdstore, np.arange(5), "K")
    npt.assert_array_equal(tdstore.magnitude, np.arange(4))
    assert tdstore.unit == b"K".ljust(1024)

@pytest.mark.xfail()
def test_set_datastore_wrong_size_silent_pass():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4, "dimensionless")
    # this should raise some sort of error because of the shape mismatch...
    with pytest.raises(ValueError):
        test_scm.library.set_datastore(tdstore, np.arange(5), "K")

def test_run_total_radiative_forcing_mode():
    inputs = ScmDataFrame(
        np.arange(10),
        index=[dt.datetime(y + 2000, 1, 1) for y in range(10)],
        columns={
            "variable": "Effective Radiative Forcing",
            "unit": "W/m^2",
            "model": "unspecified",
            "scenario": "unspecified",
            "region": "World"
        }
    )

    # check that only a single timeseries has been given at this point
    assert inputs["variable"].tolist() == ["Effective Radiative Forcing"]

    ## assumptions I think should be made by the Fortran interface (i.e. should be
    ## check in Python, not Fortran)
    # - units are correct
    # - no NaNs in input data
    # - data is on a uniform timestep

    ## these steps could be wrapped into a convenience function in future
    # allocate arrays
    test_scm.scm.initialise_total_effective_radiative_forcing_driven(inputs["time"].shape[0])

    ## TODO: check why the order of the datastore initialisation matters for getting
    ## the units of both datastores correct...
    dat_effrf_total = test_scm.effective_radiative_forcing.dat_effrf_total
    # # for some reason this contains control characters...
    # assert dat_effrf_total.unit.decode("utf-8").strip() == "W/m^2"
    # check units (should this be done inplace to save memory or safer not to?)
    # not working as units above coming out wrong
    runner = inputs.convert_unit(dat_effrf_total.unit.decode("utf-8").strip())

    dat_temperature_upper = test_scm.temperature.dat_temperature_upper
    # this fails at the moment, but passes if we initialise the datastores in the
    # opposite order (see comment in `scm.f90`)
    # assert dat_temperature_upper.unit.decode("utf-8").strip() == "K"

    dat_temperature_lower = test_scm.temperature.dat_temperature_lower
    # see above
    # assert dat_temperature_lower.unit.decode("utf-8").strip() == "K"

    dat_rndt = test_scm.temperature.dat_rndt
    # # for some reason this contains control characters...
    # assert dat_rndt.unit.decode("utf-8").strip() == "W/m^2"

    # dat_ocean_heat_uptake = test_scm.temperature.dat_ocean_heat_uptake
    # assert dat_ocean_heat_uptake.unit.decode("utf-8").strip() == "ZJ/yr"

    # check no nans (which will cause Fortran to explode)
    assert not np.isnan(inputs.values).any()
    # check uniform timestep
    assert (inputs["year"].diff().dropna() == 1).all()
    # set timestep
    assert test_scm.scm.timestep.unit.decode("utf-8").strip() == "s"
    one_year_in_seconds = 365.0 * 24 * 60 * 60
    test_scm.scm.timestep.magnitude = one_year_in_seconds

    # set inputs
    dat_effrf_total.magnitude = inputs.filter(variable="Effective Radiative Forcing").values

    # run
    test_scm.scm.run_total_radiative_forcing_driven()

    # get outputs
    def get_output_as_scmdf():
        return ScmDataFrame(
            np.vstack([
                dat_effrf_total.magnitude,
                dat_temperature_upper.magnitude,
                dat_temperature_lower.magnitude,
                dat_rndt.magnitude,
            ]).T,
            index=inputs["time"],
            columns={
                "variable": [
                    "Effective Radiative Forcing",
                    "Upper Ocean Temperature Change",
                    "Lower Ocean Temperature Change",
                    "Top of Atmosphere Net Energy Flux",
                ],
                "unit": [
                    dat_effrf_total.unit,
                    dat_temperature_upper.unit,
                    dat_temperature_lower.unit,
                    dat_rndt.unit,
                ],
                "model": "unspecified",
                "scenario": "unspecified",
                "region": "World"
            }
        )

    out = get_output_as_scmdf()


    def held_two_layer(effrf, du=50, dl=1200, lambda_0=-3.74/3, b=0.0, epsilon=1.0, eta=0.8, delta_time=one_year_in_seconds):
        C = (
            1000  # density of water (kg m^-3)
            * 4181  # heat capacity of water (J K^-1 kg^-1)
            * du  # depth of upper layer (m)
        )
        C_D = (
            1000  # density of water (kg m^-3)
            * 4181  # heat capacity of water (J K^-1 kg^-1)
            * dl  # depth of lower layer (m)
        )

        temp_upper = np.zeros_like(effrf)
        temp_lower = np.zeros_like(effrf)
        rndt = np.zeros_like(effrf)
        for i, _ in enumerate(effrf):
            if i == 0:
                continue

            exchange_term_raw = eta * (temp_upper[i - 1] - temp_lower[i - 1])

            temp_upper[i] = (
                temp_upper[i - 1]
                + delta_time
                * (
                    effrf[i - 1]
                    + (lambda_0 + b * temp_upper[i - 1]) * temp_upper[i - 1]
                    - (epsilon * exchange_term_raw)
                )
                / C
            )

            temp_lower[i] = temp_lower[i - 1] + (
                delta_time * exchange_term_raw / C
            )

            rndt[i] = (
                C * (temp_upper[i] - temp_upper[i - 1])
                + C_D * (temp_lower[i] - temp_lower[i - 1])
            ) / delta_time

        return {"temp_upper": temp_upper, "temp_lower": temp_lower, "rndt": rndt}


    python_res = held_two_layer(inputs.values.squeeze())
    npt.assert_allclose(
        out.filter(variable="Upper Ocean Temperature Change").values.squeeze(),
        python_res["temp_upper"]
    )
    npt.assert_allclose(
        out.filter(variable="Lower Ocean Temperature Change").values.squeeze(),
        python_res["temp_lower"]
    )
    npt.assert_allclose(
        out.filter(variable="Top of Atmosphere Net Energy Flux").values.squeeze(),
        python_res["rndt"]
    )


    new_du = 30.0
    # set config
    test_scm.temperature.du = new_du

    # run
    test_scm.scm.run_total_radiative_forcing_driven()

    # get outputs
    out_new_du = get_output_as_scmdf()

    python_res_new_du = held_two_layer(inputs.values.squeeze(), du=new_du)
    npt.assert_allclose(
        out_new_du.filter(variable="Upper Ocean Temperature Change").values.squeeze(),
        python_res_new_du["temp_upper"]
    )
    npt.assert_allclose(
        out_new_du.filter(variable="Lower Ocean Temperature Change").values.squeeze(),
        python_res_new_du["temp_lower"]
    )
    npt.assert_allclose(
        out_new_du.filter(variable="Top of Atmosphere Net Energy Flux").values.squeeze(),
        python_res_new_du["rndt"]
    )
