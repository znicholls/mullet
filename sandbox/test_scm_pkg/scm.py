"""
Module scm


Defined at scm.fpp lines 5-110

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging
from test_scm_pkg.datatypes import scalar

_arrays = {}
_objs = {}

def initialise_total_effective_radiative_forcing_driven(tsteps):
    """
    initialise_total_effective_radiative_forcing_driven(tsteps)
    
    
    Defined at scm.fpp lines 34-54
    
    Parameters
    ----------
    tsteps : int
    
    """
    \
        _test_scm_pkg.f90wrap_initialise_total_effective_radiative_forcing_driven(tsteps=tsteps)

def step_total_radiative_forcing_driven(i):
    """
    step_total_radiative_forcing_driven(i)
    
    
    Defined at scm.fpp lines 56-94
    
    Parameters
    ----------
    i : int
    
    """
    _test_scm_pkg.f90wrap_step_total_radiative_forcing_driven(i=i)

def run_total_radiative_forcing_driven():
    """
    run_total_radiative_forcing_driven()
    
    
    Defined at scm.fpp lines 96-110
    
    
    """
    _test_scm_pkg.f90wrap_run_total_radiative_forcing_driven()

def get_timestep():
    """
    Element timestep ftype=type(scalar) pytype=Scalar
    
    
    Defined at scm.fpp line 18
    
    """
    global timestep
    timestep_handle = _test_scm_pkg.f90wrap_scm__get__timestep()
    if tuple(timestep_handle) in _objs:
        timestep = _objs[tuple(timestep_handle)]
    else:
        timestep = scalar.from_handle(timestep_handle)
        _objs[tuple(timestep_handle)] = timestep
    return timestep

def set_timestep(timestep):
    timestep = timestep._handle
    _test_scm_pkg.f90wrap_scm__set__timestep(timestep)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "scm".')

for func in _dt_array_initialisers:
    func()
