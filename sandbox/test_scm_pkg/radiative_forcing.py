"""
Module radiative_forcing


Defined at radiative_forcing.fpp lines 5-18

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging
from test_scm_pkg.datatypes import datastore

_arrays = {}
_objs = {}

def get_dat_rf_total():
    """
    Element dat_rf_total ftype=type(datastore) pytype=Datastore
    
    
    Defined at radiative_forcing.fpp line 14
    
    """
    global dat_rf_total
    dat_rf_total_handle = \
        _test_scm_pkg.f90wrap_radiative_forcing__get__dat_rf_total()
    if tuple(dat_rf_total_handle) in _objs:
        dat_rf_total = _objs[tuple(dat_rf_total_handle)]
    else:
        dat_rf_total = datastore.from_handle(dat_rf_total_handle)
        _objs[tuple(dat_rf_total_handle)] = dat_rf_total
    return dat_rf_total

def set_dat_rf_total(dat_rf_total):
    dat_rf_total = dat_rf_total._handle
    _test_scm_pkg.f90wrap_radiative_forcing__set__dat_rf_total(dat_rf_total)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module \
        "radiative_forcing".')

for func in _dt_array_initialisers:
    func()
