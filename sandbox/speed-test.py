import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tqdm

import test_scm

SHOW_TEMP_PLOT = False

ONE_YEAR_IN_SECONDS = 365.0 * 24 * 60 * 60

def held_two_layer(effrf, du=50, dl=1200, lambda_0=-3.74/3, b=0.0, epsilon=1.0, eta=0.8, delta_time=ONE_YEAR_IN_SECONDS):
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


performance = {
    "Python": [],
    "Fortran": [],
    "Repeat": [],
    "Size of inputs": [],
}

for effrf_n in tqdm.tqdm(np.logspace(1, 5, num=5, base=10.0).astype(int), desc="effrf size"):
    for repeat in tqdm.tqdm(range(9), desc="repeats", leave=False):
        effrf = np.linspace(0, 30, effrf_n)

        start = time.time()
        python_temperature = held_two_layer(effrf)["temp_upper"]
        end = time.time()

        python_time = end - start

        # print("Python elapsed time (s): ", np.round(python_time, 6))

        start = time.time()
        test_scm.scm.initialise_total_effective_radiative_forcing_driven(effrf_n)
        test_scm.effective_radiative_forcing.dat_effrf_total.magnitude = effrf
        test_scm.scm.run_total_radiative_forcing_driven()
        fortran_temperature = np.copy(test_scm.temperature.dat_temperature_upper.magnitude)
        test_scm.datatypes.destroy_datastore(test_scm.effective_radiative_forcing.dat_effrf_total)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_temperature_upper)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_temperature_lower)
        test_scm.datatypes.destroy_datastore(test_scm.temperature.dat_rndt)
        end = time.time()
        fortran_time = end - start

        # print("Fortran elapsed time (s): ", np.round(fortran_time, 6))

        assert len(python_temperature) == len(fortran_temperature), "Python: {}, Fortran: {}".format(len(python_temperature), len(fortran_temperature))
        np.testing.assert_allclose(python_temperature, fortran_temperature, atol=1e-10)
        performance["Size of inputs"].append(effrf_n)
        performance["Repeat"].append(repeat)
        performance["Python"].append(python_time)
        performance["Fortran"].append(fortran_time)

performance = pd.DataFrame(performance).melt(
    id_vars=["Size of inputs", "Repeat"],
    value_vars=["Python", "Fortran"],
    var_name="source",
)
performance["value"] = performance["value"].astype(float)
performance["log(value)"] = np.log10(performance["value"])
performance["log(Size of inputs)"] = np.log10(performance["Size of inputs"])

sns.relplot(
    data=performance,
    x="log(Size of inputs)",
    y="log(value)",
    hue="source",
    kind="scatter",
)
plt.show()

if SHOW_TEMP_PLOT:
    plt_df = pd.DataFrame(
        np.vstack([effrf, python_temperature, fortran_temperature]).T,
        columns=["effrf", "Python", "Fortran"],
    )
    plt_df = plt_df.set_index("effrf").stack().reset_index()
    plt_df = plt_df.rename({0: "value", "level_1": "source"}, axis="columns")

    sns.relplot(
        data=plt_df,
        x="effrf",
        y="value",
        hue="source",
        kind="line",
        style="source",
        markers="source",
        markeredgecolor="none",
    )
    plt.show()
