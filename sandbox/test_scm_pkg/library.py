"""
Module library


Defined at library.fpp lines 5-26

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging

_arrays = {}
_objs = {}

def set_datastore(self, dstore_magnitude, dstore_unit):
    """
    set_datastore(self, dstore_magnitude, dstore_unit)
    
    
    Defined at library.fpp lines 15-26
    
    Parameters
    ----------
    dstore : Datastore
    dstore_magnitude : float array
    dstore_unit : str
    
    """
    _test_scm_pkg.f90wrap_set_datastore(dstore=self._handle, \
        dstore_magnitude=dstore_magnitude, dstore_unit=dstore_unit)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "library".')

for func in _dt_array_initialisers:
    func()
