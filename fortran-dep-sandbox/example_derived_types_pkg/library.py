"""
Module library


Defined at library.fpp lines 5-185

"""
from __future__ import print_function, absolute_import, division
import _example_derived_types_pkg
import f90wrap.runtime
import logging

_arrays = {}
_objs = {}

def return_value_func(val_in):
    """
    val_out = return_value_func(val_in)
    
    
    Defined at library.fpp lines 12-15
    
    Parameters
    ----------
    val_in : int
    
    Returns
    -------
    val_out : int
    
    """
    val_out = _example_derived_types_pkg.f90wrap_return_value_func(val_in=val_in)
    return val_out

def return_value_sub(val_in):
    """
    val_out = return_value_sub(val_in)
    
    
    Defined at library.fpp lines 17-21
    
    Parameters
    ----------
    val_in : int
    
    Returns
    -------
    val_out : int
    
    """
    val_out = _example_derived_types_pkg.f90wrap_return_value_sub(val_in=val_in)
    return val_out

def return_a_dt_func():
    """
    dt = return_a_dt_func()
    
    
    Defined at library.fpp lines 23-29
    
    
    Returns
    -------
    dt : Different_Types
    
    """
    dt = _example_derived_types_pkg.f90wrap_return_a_dt_func()
    dt = \
        f90wrap.runtime.lookup_class("example_derived_types_pkg.different_types").from_handle(dt)
    return dt

def do_array_stuff(n, x, y, br, co):
    """
    do_array_stuff(n, x, y, br, co)
    
    
    Defined at library.fpp lines 32-46
    
    Parameters
    ----------
    n : int
    x : float array
    y : float array
    br : float array
    co : float array
    
    """
    _example_derived_types_pkg.f90wrap_do_array_stuff(n=n, x=x, y=y, br=br, co=co)

def only_manipulate(n, array):
    """
    only_manipulate(n, array)
    
    
    Defined at library.fpp lines 48-58
    
    Parameters
    ----------
    n : int
    array : float array
    
    """
    _example_derived_types_pkg.f90wrap_only_manipulate(n=n, array=array)

def set_derived_type(dt_beta, dt_delta):
    """
    dt = set_derived_type(dt_beta, dt_delta)
    
    
    Defined at library.fpp lines 60-68
    
    Parameters
    ----------
    dt_beta : int
    dt_delta : float
    
    Returns
    -------
    dt : Different_Types
    
    """
    dt = _example_derived_types_pkg.f90wrap_set_derived_type(dt_beta=dt_beta, \
        dt_delta=dt_delta)
    dt = \
        f90wrap.runtime.lookup_class("example_derived_types_pkg.different_types").from_handle(dt)
    return dt

def modify_derived_types(self, dt2, dt3):
    """
    modify_derived_types(self, dt2, dt3)
    
    
    Defined at library.fpp lines 70-82
    
    Parameters
    ----------
    dt1 : Different_Types
    dt2 : Different_Types
    dt3 : Different_Types
    
    """
    _example_derived_types_pkg.f90wrap_modify_derived_types(dt1=self._handle, \
        dt2=dt2._handle, dt3=dt3._handle)

def modify_dertype_fixed_shape_arrays():
    """
    dertype = modify_dertype_fixed_shape_arrays()
    
    
    Defined at library.fpp lines 84-91
    
    
    Returns
    -------
    dertype : Fixed_Shape_Arrays
    
    """
    dertype = _example_derived_types_pkg.f90wrap_modify_dertype_fixed_shape_arrays()
    dertype = \
        f90wrap.runtime.lookup_class("example_derived_types_pkg.fixed_shape_arrays").from_handle(dertype)
    return dertype

def return_dertype_pointer_arrays(m, n):
    """
    dertype = return_dertype_pointer_arrays(m, n)
    
    
    Defined at library.fpp lines 93-102
    
    Parameters
    ----------
    m : int
    n : int
    
    Returns
    -------
    dertype : Pointer_Arrays
    
    """
    dertype = _example_derived_types_pkg.f90wrap_return_dertype_pointer_arrays(m=m, \
        n=n)
    dertype = \
        f90wrap.runtime.lookup_class("example_derived_types_pkg.pointer_arrays").from_handle(dertype)
    return dertype

def modify_dertype_pointer_arrays(self):
    """
    modify_dertype_pointer_arrays(self)
    
    
    Defined at library.fpp lines 104-112
    
    Parameters
    ----------
    dertype : Pointer_Arrays
    
    """
    \
        _example_derived_types_pkg.f90wrap_modify_dertype_pointer_arrays(dertype=self._handle)

def return_dertype_alloc_arrays(m, n):
    """
    dertype = return_dertype_alloc_arrays(m, n)
    
    
    Defined at library.fpp lines 114-123
    
    Parameters
    ----------
    m : int
    n : int
    
    Returns
    -------
    dertype : Alloc_Arrays
    
    """
    dertype = _example_derived_types_pkg.f90wrap_return_dertype_alloc_arrays(m=m, \
        n=n)
    dertype = \
        f90wrap.runtime.lookup_class("example_derived_types_pkg.alloc_arrays").from_handle(dertype)
    return dertype

def modify_dertype_alloc_arrays(self):
    """
    modify_dertype_alloc_arrays(self)
    
    
    Defined at library.fpp lines 125-133
    
    Parameters
    ----------
    dertype : Alloc_Arrays
    
    """
    \
        _example_derived_types_pkg.f90wrap_modify_dertype_alloc_arrays(dertype=self._handle)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "library".')

for func in _dt_array_initialisers:
    func()
