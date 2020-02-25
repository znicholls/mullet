import numpy as np
import numpy.testing as npt
import pytest

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
    test_scm.datatypes.init_datastore(tdstore, 4)
    assert isinstance(tdstore.magnitude, np.ndarray)

def test_set_datastore_allocated_array():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4)
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
    test_scm.datatypes.init_datastore(tdstore, 4)
    test_scm.library.set_datastore(tdstore, np.arange(4), "K")
    npt.assert_array_equal(tdstore.magnitude, np.arange(4))
    assert tdstore.unit == b"K".ljust(1024)

def test_set_datastore_wrong_size():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4)
    test_scm.library.set_datastore(tdstore, np.arange(5), "K")
    npt.assert_array_equal(tdstore.magnitude, np.arange(4))
    assert tdstore.unit == b"K".ljust(1024)

@pytest.mark.xfail()
def test_set_datastore_wrong_size_silent_pass():
    tdstore = test_scm.Datatypes.datastore()
    test_scm.datatypes.init_datastore(tdstore, 4)
    # this should raise some sort of error because of the shape mismatch...
    with pytest.raises(ValueError):
        test_scm.library.set_datastore(tdstore, np.arange(5), "K")
