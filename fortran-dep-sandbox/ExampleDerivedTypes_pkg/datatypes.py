"""
Module datatypes


Defined at datatypes.fpp lines 39-110

"""
from __future__ import print_function, absolute_import, division
import _ExampleDerivedTypes_pkg
import f90wrap.runtime
import logging
from ExampleDerivedTypes_pkg.datatypes_allocatable import alloc_arrays

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.different_types")
class different_types(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=different_types)
    
    
    Defined at datatypes.fpp lines 54-58
    
    """
    def __init__(self, handle=None):
        """
        self = Different_Types()
        
        
        Defined at datatypes.fpp lines 54-58
        
        
        Returns
        -------
        this : Different_Types
        	Object to be constructed
        
        
        Automatically generated constructor for different_types
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_different_types_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Different_Types
        
        
        Defined at datatypes.fpp lines 54-58
        
        Parameters
        ----------
        this : Different_Types
        	Object to be destructed
        
        
        Automatically generated destructor for different_types
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_different_types_finalise(this=self._handle)
    
    @property
    def alpha(self):
        """
        Element alpha ftype=logical pytype=bool
        
        
        Defined at datatypes.fpp line 55
        
        """
        return \
            _ExampleDerivedTypes_pkg.f90wrap_different_types__get__alpha(self._handle)
    
    @alpha.setter
    def alpha(self, alpha):
        _ExampleDerivedTypes_pkg.f90wrap_different_types__set__alpha(self._handle, \
            alpha)
    
    @property
    def beta(self):
        """
        Element beta ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 56
        
        """
        return _ExampleDerivedTypes_pkg.f90wrap_different_types__get__beta(self._handle)
    
    @beta.setter
    def beta(self, beta):
        _ExampleDerivedTypes_pkg.f90wrap_different_types__set__beta(self._handle, beta)
    
    @property
    def delta(self):
        """
        Element delta ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 57
        
        """
        return \
            _ExampleDerivedTypes_pkg.f90wrap_different_types__get__delta(self._handle)
    
    @delta.setter
    def delta(self, delta):
        _ExampleDerivedTypes_pkg.f90wrap_different_types__set__delta(self._handle, \
            delta)
    
    def __str__(self):
        ret = ['<different_types>{\n']
        ret.append('    alpha : ')
        ret.append(repr(self.alpha))
        ret.append(',\n    beta : ')
        ret.append(repr(self.beta))
        ret.append(',\n    delta : ')
        ret.append(repr(self.delta))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.fixed_shape_arrays")
class fixed_shape_arrays(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=fixed_shape_arrays)
    
    
    Defined at datatypes.fpp lines 61-65
    
    """
    def __init__(self, handle=None):
        """
        self = Fixed_Shape_Arrays()
        
        
        Defined at datatypes.fpp lines 61-65
        
        
        Returns
        -------
        this : Fixed_Shape_Arrays
        	Object to be constructed
        
        
        Automatically generated constructor for fixed_shape_arrays
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Fixed_Shape_Arrays
        
        
        Defined at datatypes.fpp lines 61-65
        
        Parameters
        ----------
        this : Fixed_Shape_Arrays
        	Object to be destructed
        
        
        Automatically generated destructor for fixed_shape_arrays
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays_finalise(this=self._handle)
    
    @property
    def eta(self):
        """
        Element eta ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 62
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__eta(self._handle)
        if array_handle in self._arrays:
            eta = self._arrays[array_handle]
        else:
            eta = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__eta)
            self._arrays[array_handle] = eta
        return eta
    
    @eta.setter
    def eta(self, eta):
        self.eta[...] = eta
    
    @property
    def theta(self):
        """
        Element theta ftype=real(isp) pytype=float
        
        
        Defined at datatypes.fpp line 63
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__theta(self._handle)
        if array_handle in self._arrays:
            theta = self._arrays[array_handle]
        else:
            theta = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__theta)
            self._arrays[array_handle] = theta
        return theta
    
    @theta.setter
    def theta(self, theta):
        self.theta[...] = theta
    
    @property
    def iota(self):
        """
        Element iota ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 64
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__iota(self._handle)
        if array_handle in self._arrays:
            iota = self._arrays[array_handle]
        else:
            iota = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_fixed_shape_arrays__array__iota)
            self._arrays[array_handle] = iota
        return iota
    
    @iota.setter
    def iota(self, iota):
        self.iota[...] = iota
    
    def __str__(self):
        ret = ['<fixed_shape_arrays>{\n']
        ret.append('    eta : ')
        ret.append(repr(self.eta))
        ret.append(',\n    theta : ')
        ret.append(repr(self.theta))
        ret.append(',\n    iota : ')
        ret.append(repr(self.iota))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.nested")
class nested(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=nested)
    
    
    Defined at datatypes.fpp lines 67-70
    
    """
    def __init__(self, handle=None):
        """
        self = Nested()
        
        
        Defined at datatypes.fpp lines 67-70
        
        
        Returns
        -------
        this : Nested
        	Object to be constructed
        
        
        Automatically generated constructor for nested
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_nested_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Nested
        
        
        Defined at datatypes.fpp lines 67-70
        
        Parameters
        ----------
        this : Nested
        	Object to be destructed
        
        
        Automatically generated destructor for nested
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_nested_finalise(this=self._handle)
    
    @property
    def mu(self):
        """
        Element mu ftype=type(different_types) pytype=Different_Types
        
        
        Defined at datatypes.fpp line 68
        
        """
        mu_handle = _ExampleDerivedTypes_pkg.f90wrap_nested__get__mu(self._handle)
        if tuple(mu_handle) in self._objs:
            mu = self._objs[tuple(mu_handle)]
        else:
            mu = different_types.from_handle(mu_handle)
            self._objs[tuple(mu_handle)] = mu
        return mu
    
    @mu.setter
    def mu(self, mu):
        mu = mu._handle
        _ExampleDerivedTypes_pkg.f90wrap_nested__set__mu(self._handle, mu)
    
    @property
    def nu(self):
        """
        Element nu ftype=type(fixed_shape_arrays) pytype=Fixed_Shape_Arrays
        
        
        Defined at datatypes.fpp line 69
        
        """
        nu_handle = _ExampleDerivedTypes_pkg.f90wrap_nested__get__nu(self._handle)
        if tuple(nu_handle) in self._objs:
            nu = self._objs[tuple(nu_handle)]
        else:
            nu = fixed_shape_arrays.from_handle(nu_handle)
            self._objs[tuple(nu_handle)] = nu
        return nu
    
    @nu.setter
    def nu(self, nu):
        nu = nu._handle
        _ExampleDerivedTypes_pkg.f90wrap_nested__set__nu(self._handle, nu)
    
    def __str__(self):
        ret = ['<nested>{\n']
        ret.append('    mu : ')
        ret.append(repr(self.mu))
        ret.append(',\n    nu : ')
        ret.append(repr(self.nu))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.pointer_arrays")
class pointer_arrays(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=pointer_arrays)
    
    
    Defined at datatypes.fpp lines 73-78
    
    """
    def __init__(self, handle=None):
        """
        self = Pointer_Arrays()
        
        
        Defined at datatypes.fpp lines 73-78
        
        
        Returns
        -------
        this : Pointer_Arrays
        	Object to be constructed
        
        
        Automatically generated constructor for pointer_arrays
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Pointer_Arrays
        
        
        Defined at datatypes.fpp lines 73-78
        
        Parameters
        ----------
        this : Pointer_Arrays
        	Object to be destructed
        
        
        Automatically generated destructor for pointer_arrays
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays_finalise(this=self._handle)
    
    @property
    def chi(self):
        """
        Element chi ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 74
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__chi(self._handle)
        if array_handle in self._arrays:
            chi = self._arrays[array_handle]
        else:
            chi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__chi)
            self._arrays[array_handle] = chi
        return chi
    
    @chi.setter
    def chi(self, chi):
        self.chi[...] = chi
    
    @property
    def psi(self):
        """
        Element psi ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 75
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__psi(self._handle)
        if array_handle in self._arrays:
            psi = self._arrays[array_handle]
        else:
            psi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__psi)
            self._arrays[array_handle] = psi
        return psi
    
    @psi.setter
    def psi(self, psi):
        self.psi[...] = psi
    
    @property
    def chi_shape(self):
        """
        Element chi_shape ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 76
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__chi_shape(self._handle)
        if array_handle in self._arrays:
            chi_shape = self._arrays[array_handle]
        else:
            chi_shape = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__chi_shape)
            self._arrays[array_handle] = chi_shape
        return chi_shape
    
    @chi_shape.setter
    def chi_shape(self, chi_shape):
        self.chi_shape[...] = chi_shape
    
    @property
    def psi_shape(self):
        """
        Element psi_shape ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 77
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__psi_shape(self._handle)
        if array_handle in self._arrays:
            psi_shape = self._arrays[array_handle]
        else:
            psi_shape = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_pointer_arrays__array__psi_shape)
            self._arrays[array_handle] = psi_shape
        return psi_shape
    
    @psi_shape.setter
    def psi_shape(self, psi_shape):
        self.psi_shape[...] = psi_shape
    
    def __str__(self):
        ret = ['<pointer_arrays>{\n']
        ret.append('    chi : ')
        ret.append(repr(self.chi))
        ret.append(',\n    psi : ')
        ret.append(repr(self.psi))
        ret.append(',\n    chi_shape : ')
        ret.append(repr(self.chi_shape))
        ret.append(',\n    psi_shape : ')
        ret.append(repr(self.psi_shape))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.alloc_arrays_2")
class alloc_arrays_2(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=alloc_arrays_2)
    
    
    Defined at datatypes.fpp lines 81-86
    
    """
    def __init__(self, handle=None):
        """
        self = Alloc_Arrays_2()
        
        
        Defined at datatypes.fpp lines 81-86
        
        
        Returns
        -------
        this : Alloc_Arrays_2
        	Object to be constructed
        
        
        Automatically generated constructor for alloc_arrays_2
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Alloc_Arrays_2
        
        
        Defined at datatypes.fpp lines 81-86
        
        Parameters
        ----------
        this : Alloc_Arrays_2
        	Object to be destructed
        
        
        Automatically generated destructor for alloc_arrays_2
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2_finalise(this=self._handle)
    
    @property
    def chi(self):
        """
        Element chi ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 82
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__chi(self._handle)
        if array_handle in self._arrays:
            chi = self._arrays[array_handle]
        else:
            chi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__chi)
            self._arrays[array_handle] = chi
        return chi
    
    @chi.setter
    def chi(self, chi):
        self.chi[...] = chi
    
    @property
    def psi(self):
        """
        Element psi ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 83
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__psi(self._handle)
        if array_handle in self._arrays:
            psi = self._arrays[array_handle]
        else:
            psi = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__psi)
            self._arrays[array_handle] = psi
        return psi
    
    @psi.setter
    def psi(self, psi):
        self.psi[...] = psi
    
    @property
    def chi_shape(self):
        """
        Element chi_shape ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 84
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__chi_shape(self._handle)
        if array_handle in self._arrays:
            chi_shape = self._arrays[array_handle]
        else:
            chi_shape = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__chi_shape)
            self._arrays[array_handle] = chi_shape
        return chi_shape
    
    @chi_shape.setter
    def chi_shape(self, chi_shape):
        self.chi_shape[...] = chi_shape
    
    @property
    def psi_shape(self):
        """
        Element psi_shape ftype=integer(4) pytype=int
        
        
        Defined at datatypes.fpp line 85
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__psi_shape(self._handle)
        if array_handle in self._arrays:
            psi_shape = self._arrays[array_handle]
        else:
            psi_shape = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _ExampleDerivedTypes_pkg.f90wrap_alloc_arrays_2__array__psi_shape)
            self._arrays[array_handle] = psi_shape
        return psi_shape
    
    @psi_shape.setter
    def psi_shape(self, psi_shape):
        self.psi_shape[...] = psi_shape
    
    def __str__(self):
        ret = ['<alloc_arrays_2>{\n']
        ret.append('    chi : ')
        ret.append(repr(self.chi))
        ret.append(',\n    psi : ')
        ret.append(repr(self.psi))
        ret.append(',\n    chi_shape : ')
        ret.append(repr(self.chi_shape))
        ret.append(',\n    psi_shape : ')
        ret.append(repr(self.psi_shape))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("ExampleDerivedTypes_pkg.array_nested")
class array_nested(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=array_nested)
    
    
    Defined at datatypes.fpp lines 88-92
    
    """
    def __init__(self, handle=None):
        """
        self = Array_Nested()
        
        
        Defined at datatypes.fpp lines 88-92
        
        
        Returns
        -------
        this : Array_Nested
        	Object to be constructed
        
        
        Automatically generated constructor for array_nested
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _ExampleDerivedTypes_pkg.f90wrap_array_nested_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Array_Nested
        
        
        Defined at datatypes.fpp lines 88-92
        
        Parameters
        ----------
        this : Array_Nested
        	Object to be destructed
        
        
        Automatically generated destructor for array_nested
        """
        if self._alloc:
            _ExampleDerivedTypes_pkg.f90wrap_array_nested_finalise(this=self._handle)
    
    def init_array_xi(self):
        self.xi = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_getitem__xi,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_setitem__xi,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_len__xi,
                                        """
        Element xi ftype=type(different_types) pytype=Different_Types
        
        
        Defined at datatypes.fpp line 89
        
        """, different_types)
        return self.xi
    
    def init_array_omicron(self):
        self.omicron = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_getitem__omicron,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_setitem__omicron,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_len__omicron,
                                        """
        Element omicron ftype=type(fixed_shape_arrays) pytype=Fixed_Shape_Arrays
        
        
        Defined at datatypes.fpp line 90
        
        """, fixed_shape_arrays)
        return self.omicron
    
    def init_array_pi(self):
        self.pi = f90wrap.runtime.FortranDerivedTypeArray(self,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_getitem__pi,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_setitem__pi,
                                        _ExampleDerivedTypes_pkg.f90wrap_array_nested__array_len__pi,
                                        """
        Element pi ftype=type(alloc_arrays) pytype=Alloc_Arrays
        
        
        Defined at datatypes.fpp line 91
        
        """, alloc_arrays)
        return self.pi
    
    _dt_array_initialisers = [init_array_xi, init_array_omicron, init_array_pi]
    

def init_array_nested(self, size_bn):
    """
    init_array_nested(self, size_bn)
    
    
    Defined at datatypes.fpp lines 96-102
    
    Parameters
    ----------
    dertype : Array_Nested
    size_bn : int
    
    """
    _ExampleDerivedTypes_pkg.f90wrap_init_array_nested(dertype=self._handle, \
        size_bn=size_bn)

def destroy_array_nested(self):
    """
    destroy_array_nested(self)
    
    
    Defined at datatypes.fpp lines 104-109
    
    Parameters
    ----------
    dertype : Array_Nested
    
    """
    _ExampleDerivedTypes_pkg.f90wrap_destroy_array_nested(dertype=self._handle)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "datatypes".')

for func in _dt_array_initialisers:
    func()
