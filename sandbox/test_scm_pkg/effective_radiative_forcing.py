"""
Module effective_radiative_forcing


Defined at effective_radiative_forcing.fpp lines 5-18

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging
from test_scm_pkg.datatypes import datastore

_arrays = {}
_objs = {}

def get_dat_effrf_total():
    """
    Element dat_effrf_total ftype=type(datastore) pytype=Datastore
    
    
    Defined at effective_radiative_forcing.fpp line 14
    
    """
    global dat_effrf_total
    dat_effrf_total_handle = \
        _test_scm_pkg.f90wrap_effective_radiative_forcing__get__dat_effrf_total()
    if tuple(dat_effrf_total_handle) in _objs:
        dat_effrf_total = _objs[tuple(dat_effrf_total_handle)]
    else:
        dat_effrf_total = datastore.from_handle(dat_effrf_total_handle)
        _objs[tuple(dat_effrf_total_handle)] = dat_effrf_total
    return dat_effrf_total

def set_dat_effrf_total(dat_effrf_total):
    dat_effrf_total = dat_effrf_total._handle
    \
        _test_scm_pkg.f90wrap_effective_radiative_forcing__set__dat_effrf_total(dat_effrf_total)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module \
        "effective_radiative_forcing".')

for func in _dt_array_initialisers:
    func()
