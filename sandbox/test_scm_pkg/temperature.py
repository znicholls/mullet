"""
Module temperature


Defined at temperature.fpp lines 5-81

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging
from test_scm_pkg.datatypes import datastore

_arrays = {}
_objs = {}

def temp_response_held_two_layer(effrf, tu, tl, delta_t):
    """
    temp_response_held_two_layer = temp_response_held_two_layer(effrf, tu, tl, \
        delta_t)
    
    
    Defined at temperature.fpp lines 43-81
    
    Parameters
    ----------
    effrf : float
    tu : float
    tl : float
    delta_t : float
    
    Returns
    -------
    temp_response_held_two_layer : float array
    
    """
    temp_response_held_two_layer = \
        _test_scm_pkg.f90wrap_temp_response_held_two_layer(effrf=effrf, tu=tu, \
        tl=tl, delta_t=delta_t)
    return temp_response_held_two_layer

def get_dat_temperature_upper():
    """
    Element dat_temperature_upper ftype=type(datastore) pytype=Datastore
    
    
    Defined at temperature.fpp line 25
    
    """
    global dat_temperature_upper
    dat_temperature_upper_handle = \
        _test_scm_pkg.f90wrap_temperature__get__dat_temperature_upper()
    if tuple(dat_temperature_upper_handle) in _objs:
        dat_temperature_upper = _objs[tuple(dat_temperature_upper_handle)]
    else:
        dat_temperature_upper = datastore.from_handle(dat_temperature_upper_handle)
        _objs[tuple(dat_temperature_upper_handle)] = dat_temperature_upper
    return dat_temperature_upper

def set_dat_temperature_upper(dat_temperature_upper):
    dat_temperature_upper = dat_temperature_upper._handle
    \
        _test_scm_pkg.f90wrap_temperature__set__dat_temperature_upper(dat_temperature_upper)

def get_dat_temperature_lower():
    """
    Element dat_temperature_lower ftype=type(datastore) pytype=Datastore
    
    
    Defined at temperature.fpp line 26
    
    """
    global dat_temperature_lower
    dat_temperature_lower_handle = \
        _test_scm_pkg.f90wrap_temperature__get__dat_temperature_lower()
    if tuple(dat_temperature_lower_handle) in _objs:
        dat_temperature_lower = _objs[tuple(dat_temperature_lower_handle)]
    else:
        dat_temperature_lower = datastore.from_handle(dat_temperature_lower_handle)
        _objs[tuple(dat_temperature_lower_handle)] = dat_temperature_lower
    return dat_temperature_lower

def set_dat_temperature_lower(dat_temperature_lower):
    dat_temperature_lower = dat_temperature_lower._handle
    \
        _test_scm_pkg.f90wrap_temperature__set__dat_temperature_lower(dat_temperature_lower)

def get_dat_ocean_heat_uptake():
    """
    Element dat_ocean_heat_uptake ftype=type(datastore) pytype=Datastore
    
    
    Defined at temperature.fpp line 27
    
    """
    global dat_ocean_heat_uptake
    dat_ocean_heat_uptake_handle = \
        _test_scm_pkg.f90wrap_temperature__get__dat_ocean_heat_uptake()
    if tuple(dat_ocean_heat_uptake_handle) in _objs:
        dat_ocean_heat_uptake = _objs[tuple(dat_ocean_heat_uptake_handle)]
    else:
        dat_ocean_heat_uptake = datastore.from_handle(dat_ocean_heat_uptake_handle)
        _objs[tuple(dat_ocean_heat_uptake_handle)] = dat_ocean_heat_uptake
    return dat_ocean_heat_uptake

def set_dat_ocean_heat_uptake(dat_ocean_heat_uptake):
    dat_ocean_heat_uptake = dat_ocean_heat_uptake._handle
    \
        _test_scm_pkg.f90wrap_temperature__set__dat_ocean_heat_uptake(dat_ocean_heat_uptake)

def get_dat_rndt():
    """
    Element dat_rndt ftype=type(datastore) pytype=Datastore
    
    
    Defined at temperature.fpp line 28
    
    """
    global dat_rndt
    dat_rndt_handle = _test_scm_pkg.f90wrap_temperature__get__dat_rndt()
    if tuple(dat_rndt_handle) in _objs:
        dat_rndt = _objs[tuple(dat_rndt_handle)]
    else:
        dat_rndt = datastore.from_handle(dat_rndt_handle)
        _objs[tuple(dat_rndt_handle)] = dat_rndt
    return dat_rndt

def set_dat_rndt(dat_rndt):
    dat_rndt = dat_rndt._handle
    _test_scm_pkg.f90wrap_temperature__set__dat_rndt(dat_rndt)

def get_du():
    """
    Element du ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 34
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__du()

def set_du(du):
    _test_scm_pkg.f90wrap_temperature__set__du(du)

def get_dl():
    """
    Element dl ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 35
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__dl()

def set_dl(dl):
    _test_scm_pkg.f90wrap_temperature__set__dl(dl)

def get_lambda_0():
    """
    Element lambda_0 ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 36
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__lambda_0()

def set_lambda_0(lambda_0):
    _test_scm_pkg.f90wrap_temperature__set__lambda_0(lambda_0)

def get_b():
    """
    Element b ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 37
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__b()

def set_b(b):
    _test_scm_pkg.f90wrap_temperature__set__b(b)

def get_epsilon():
    """
    Element epsilon ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 38
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__epsilon()

def set_epsilon(epsilon):
    _test_scm_pkg.f90wrap_temperature__set__epsilon(epsilon)

def get_eta():
    """
    Element eta ftype=real(idp) pytype=float
    
    
    Defined at temperature.fpp line 39
    
    """
    return _test_scm_pkg.f90wrap_temperature__get__eta()

def set_eta(eta):
    _test_scm_pkg.f90wrap_temperature__set__eta(eta)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module \
        "temperature".')

for func in _dt_array_initialisers:
    func()
