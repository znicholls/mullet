"""
Module datatypes


Defined at datatypes.fpp lines 5-44

"""
from __future__ import print_function, absolute_import, division
import _test_scm_pkg
import f90wrap.runtime
import logging

_arrays = {}
_objs = {}

@f90wrap.runtime.register_class("test_scm_pkg.scalar")
class scalar(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=scalar)
    
    
    Defined at datatypes.fpp lines 13-17
    
    """
    def __init__(self, handle=None):
        """
        self = Scalar()
        
        
        Defined at datatypes.fpp lines 13-17
        
        
        Returns
        -------
        this : Scalar
        	Object to be constructed
        
        
        Automatically generated constructor for scalar
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _test_scm_pkg.f90wrap_scalar_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Scalar
        
        
        Defined at datatypes.fpp lines 13-17
        
        Parameters
        ----------
        this : Scalar
        	Object to be destructed
        
        
        Automatically generated destructor for scalar
        """
        if self._alloc:
            _test_scm_pkg.f90wrap_scalar_finalise(this=self._handle)
    
    @property
    def unit(self):
        """
        Element unit ftype=character(len = 50) pytype=str
        
        
        Defined at datatypes.fpp line 14
        
        """
        return _test_scm_pkg.f90wrap_scalar__get__unit(self._handle)
    
    @unit.setter
    def unit(self, unit):
        _test_scm_pkg.f90wrap_scalar__set__unit(self._handle, unit)
    
    @property
    def comments(self):
        """
        Element comments ftype=character(len = 50) pytype=str
        
        
        Defined at datatypes.fpp line 15
        
        """
        return _test_scm_pkg.f90wrap_scalar__get__comments(self._handle)
    
    @comments.setter
    def comments(self, comments):
        _test_scm_pkg.f90wrap_scalar__set__comments(self._handle, comments)
    
    @property
    def magnitude(self):
        """
        Element magnitude ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 16
        
        """
        return _test_scm_pkg.f90wrap_scalar__get__magnitude(self._handle)
    
    @magnitude.setter
    def magnitude(self, magnitude):
        _test_scm_pkg.f90wrap_scalar__set__magnitude(self._handle, magnitude)
    
    def __str__(self):
        ret = ['<scalar>{\n']
        ret.append('    unit : ')
        ret.append(repr(self.unit))
        ret.append(',\n    comments : ')
        ret.append(repr(self.comments))
        ret.append(',\n    magnitude : ')
        ret.append(repr(self.magnitude))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

@f90wrap.runtime.register_class("test_scm_pkg.datastore")
class datastore(f90wrap.runtime.FortranDerivedType):
    """
    Type(name=datastore)
    
    
    Defined at datatypes.fpp lines 19-23
    
    """
    def __init__(self, handle=None):
        """
        self = Datastore()
        
        
        Defined at datatypes.fpp lines 19-23
        
        
        Returns
        -------
        this : Datastore
        	Object to be constructed
        
        
        Automatically generated constructor for datastore
        """
        f90wrap.runtime.FortranDerivedType.__init__(self)
        result = _test_scm_pkg.f90wrap_datastore_initialise()
        self._handle = result[0] if isinstance(result, tuple) else result
    
    def __del__(self):
        """
        Destructor for class Datastore
        
        
        Defined at datatypes.fpp lines 19-23
        
        Parameters
        ----------
        this : Datastore
        	Object to be destructed
        
        
        Automatically generated destructor for datastore
        """
        if self._alloc:
            _test_scm_pkg.f90wrap_datastore_finalise(this=self._handle)
    
    @property
    def unit(self):
        """
        Element unit ftype=character(len = 50) pytype=str
        
        
        Defined at datatypes.fpp line 20
        
        """
        return _test_scm_pkg.f90wrap_datastore__get__unit(self._handle)
    
    @unit.setter
    def unit(self, unit):
        _test_scm_pkg.f90wrap_datastore__set__unit(self._handle, unit)
    
    @property
    def comments(self):
        """
        Element comments ftype=character(len = 50) pytype=str
        
        
        Defined at datatypes.fpp line 21
        
        """
        return _test_scm_pkg.f90wrap_datastore__get__comments(self._handle)
    
    @comments.setter
    def comments(self, comments):
        _test_scm_pkg.f90wrap_datastore__set__comments(self._handle, comments)
    
    @property
    def magnitude(self):
        """
        Element magnitude ftype=real(idp) pytype=float
        
        
        Defined at datatypes.fpp line 22
        
        """
        array_ndim, array_type, array_shape, array_handle = \
            _test_scm_pkg.f90wrap_datastore__array__magnitude(self._handle)
        if array_handle in self._arrays:
            magnitude = self._arrays[array_handle]
        else:
            magnitude = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                    self._handle,
                                    _test_scm_pkg.f90wrap_datastore__array__magnitude)
            self._arrays[array_handle] = magnitude
        return magnitude
    
    @magnitude.setter
    def magnitude(self, magnitude):
        self.magnitude[...] = magnitude
    
    def __str__(self):
        ret = ['<datastore>{\n']
        ret.append('    unit : ')
        ret.append(repr(self.unit))
        ret.append(',\n    comments : ')
        ret.append(repr(self.comments))
        ret.append(',\n    magnitude : ')
        ret.append(repr(self.magnitude))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

def init_datastore(self, tsteps, dsunit):
    """
    init_datastore(self, tsteps, dsunit)
    
    
    Defined at datatypes.fpp lines 27-36
    
    Parameters
    ----------
    dstore : Datastore
    tsteps : int
    dsunit : str
    
    """
    _test_scm_pkg.f90wrap_init_datastore(dstore=self._handle, tsteps=tsteps, \
        dsunit=dsunit)

def destroy_datastore(self):
    """
    destroy_datastore(self)
    
    
    Defined at datatypes.fpp lines 38-44
    
    Parameters
    ----------
    dstore : Datastore
    
    """
    _test_scm_pkg.f90wrap_destroy_datastore(dstore=self._handle)


_array_initialisers = []
_dt_array_initialisers = []

try:
    for func in _array_initialisers:
        func()
except ValueError:
    logging.debug('unallocated array(s) detected on import of module "datatypes".')

for func in _dt_array_initialisers:
    func()
