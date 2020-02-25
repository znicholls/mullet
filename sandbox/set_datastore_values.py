import numpy as np

import test_scm

TSTEPS = 4

EXAMPLE_DATASTORE = test_scm.Datatypes.datastore()

try:
    EXAMPLE_DATASTORE.magnitude
except ValueError:
    print("Requesting magnitude without allocating explodes")

try:
    EXAMPLE_DATASTORE.magnitude = np.arange(TSTEPS)
except ValueError:
    print("Setting magnitude without allocating explodes")

print("Init datastore")
test_scm.datatypes.init_datastore(EXAMPLE_DATASTORE, TSTEPS)

print("Magnitude is now: {}".format(EXAMPLE_DATASTORE.magnitude))

print("Alter magnitude value from Python")
EXAMPLE_DATASTORE.magnitude = np.arange(TSTEPS)

print("Magnitude is now: {}".format(EXAMPLE_DATASTORE.magnitude))
