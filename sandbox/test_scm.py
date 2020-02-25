from __future__ import print_function, absolute_import, division
import _test_scm
import f90wrap.runtime
import logging

class Datatypes(f90wrap.runtime.FortranModule):
    """
    Module datatypes
    
    
    Defined at datatypes.fpp lines 5-36
    
    """
    @f90wrap.runtime.register_class("test_scm.datastore")
    class datastore(f90wrap.runtime.FortranDerivedType):
        """
        Type(name=datastore)
        
        
        Defined at datatypes.fpp lines 13-17
        
        """
        def __init__(self, handle=None):
            """
            self = Datastore()
            
            
            Defined at datatypes.fpp lines 13-17
            
            
            Returns
            -------
            this : Datastore
            	Object to be constructed
            
            
            Automatically generated constructor for datastore
            """
            f90wrap.runtime.FortranDerivedType.__init__(self)
            result = _test_scm.f90wrap_datastore_initialise()
            self._handle = result[0] if isinstance(result, tuple) else result
        
        def __del__(self):
            """
            Destructor for class Datastore
            
            
            Defined at datatypes.fpp lines 13-17
            
            Parameters
            ----------
            this : Datastore
            	Object to be destructed
            
            
            Automatically generated destructor for datastore
            """
            if self._alloc:
                _test_scm.f90wrap_datastore_finalise(this=self._handle)
        
        @property
        def unit(self):
            """
            Element unit ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 14
            
            """
            return _test_scm.f90wrap_datastore__get__unit(self._handle)
        
        @unit.setter
        def unit(self, unit):
            _test_scm.f90wrap_datastore__set__unit(self._handle, unit)
        
        @property
        def comments(self):
            """
            Element comments ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 15
            
            """
            return _test_scm.f90wrap_datastore__get__comments(self._handle)
        
        @comments.setter
        def comments(self, comments):
            _test_scm.f90wrap_datastore__set__comments(self._handle, comments)
        
        @property
        def magnitude(self):
            """
            Element magnitude ftype=real(idp) pytype=float
            
            
            Defined at datatypes.fpp line 16
            
            """
            array_ndim, array_type, array_shape, array_handle = \
                _test_scm.f90wrap_datastore__array__magnitude(self._handle)
            if array_handle in self._arrays:
                magnitude = self._arrays[array_handle]
            else:
                magnitude = f90wrap.runtime.get_array(f90wrap.runtime.sizeof_fortran_t,
                                        self._handle,
                                        _test_scm.f90wrap_datastore__array__magnitude)
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
        
    
    @staticmethod
    def init_datastore(self, tsteps):
        """
        init_datastore(self, tsteps)
        
        
        Defined at datatypes.fpp lines 21-28
        
        Parameters
        ----------
        dstore : Datastore
        tsteps : int
        
        """
        _test_scm.f90wrap_init_datastore(dstore=self._handle, tsteps=tsteps)
    
    @staticmethod
    def destroy_datastore(self):
        """
        destroy_datastore(self)
        
        
        Defined at datatypes.fpp lines 30-36
        
        Parameters
        ----------
        dstore : Datastore
        
        """
        _test_scm.f90wrap_destroy_datastore(dstore=self._handle)
    
    _dt_array_initialisers = []
    

datatypes = Datatypes()

class Library(f90wrap.runtime.FortranModule):
    """
    Module library
    
    
    Defined at library.fpp lines 5-26
    
    """
    pass
    _dt_array_initialisers = []
    

library = Library()

