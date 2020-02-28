import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tqdm

import test_scm

SHOW_TEMP_PLOT = False

ONE_YEAR_IN_SECONDS = 365.0 * 24 * 60 * 60

def held_two_layer(EFFRF, du=50, dl=1200, lambda_0=-3.74/3, b=0.0, epsilon=1.0, eta=0.8, delta_time=ONE_YEAR_IN_SECONDS):
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

    temp_upper = np.zeros_like(EFFRF)
    temp_lower = np.zeros_like(EFFRF)
    rndt = np.zeros_like(EFFRF)
    for i, _ in enumerate(EFFRF):
        if i == 0:
            continue

        exchange_term_raw = eta * (temp_upper[i - 1] - temp_lower[i - 1])

        temp_upper[i] = (
            temp_upper[i - 1]
            + delta_time
            * (
                EFFRF[i - 1]
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


performance = {
    "Python": [],
    "Fortran": [],
    "Repeat": [],
    "Number of parameter sets": [],
}

EFFRF_N = 10**3
EFFRF = np.linspace(0, 8, EFFRF_N)

for para_n in tqdm.tqdm(np.logspace(1, 4, num=4, base=10.0).astype(int), desc="number of parameter sets to run"):
    for repeat in tqdm.tqdm(range(2), desc="repeats", leave=False):
        lambdas = np.linspace(-3.74 / 3.0, -3.74/4.0, para_n)

        fortran_temperatures = []
        start = time.time()
        test_scm.scm.initialise_total_effective_radiative_forcing_driven(EFFRF_N)
        test_scm.effective_radiative_forcing.dat_effrf_total.magnitude = EFFRF
        for lambda_0 in lambdas:
            test_scm.temperature.lambda_0 = lambda_0
            test_scm.scm.run_total_radiative_forcing_driven()
            fortran_temperatures.append(np.copy(test_scm.temperature.dat_temperature_upper.magnitude))

        test_scm.datatypes.destroy_datastore(test_scm.effective_radiative_forcing.dat_effrf_total)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_temperature_upper)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_temperature_lower)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_rndt)
        end = time.time()
        fortran_time = end - start

        if para_n <= 10**2:
            python_temperatures = []
            start = time.time()
            for lambda_0 in lambdas:
                python_temperatures.append(held_two_layer(EFFRF, lambda_0=lambda_0)["temp_upper"])
            end = time.time()

            python_time = end - start

            assert len(python_temperatures[0]) == len(fortran_temperatures[0]), "Python: {}, Fortran: {}".format(len(python_temperatures[0]), len(fortran_temperatures[0]))

            python_temperatures_test = np.vstack(python_temperatures)
            fortran_temperatures_test = np.vstack(fortran_temperatures)
            assert python_temperatures_test.shape == fortran_temperatures_test.shape
            np.testing.assert_allclose(
                python_temperatures_test,
                fortran_temperatures_test,
            )

            if SHOW_TEMP_PLOT:
                fig = plt.figure()
                ax = fig.add_subplot(111)
                ax = pd.DataFrame(python_temperatures_test).T.plot(ax=ax, color="blue", linewidth=0.5)
                ax = pd.DataFrame(fortran_temperatures_test).T.plot(ax=ax, color="red", linewidth=0.5, linestyle="--")
                plt.show()

        else:
            python_time = np.nan

        performance["Number of parameter sets"].append(para_n)
        performance["Repeat"].append(repeat)
        performance["Python"].append(python_time)
        performance["Fortran"].append(fortran_time)

performance = pd.DataFrame(performance).melt(
    id_vars=["Number of parameter sets", "Repeat"],
    value_vars=["Python", "Fortran"],
    var_name="source",
)
performance["value"] = performance["value"].astype(float)
performance["log(value)"] = np.log10(performance["value"])
performance["log(Number of parameter sets)"] = np.log10(performance["Number of parameter sets"])

sns.relplot(
    data=performance,
    x="log(Number of parameter sets)",
    y="log(value)",
    hue="source",
    kind="scatter",
)
plt.show()
