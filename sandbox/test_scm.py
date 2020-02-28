from __future__ import print_function, absolute_import, division
import _test_scm
import f90wrap.runtime
import logging

class Datatypes(f90wrap.runtime.FortranModule):
    """
    Module datatypes
    
    
    Defined at datatypes.fpp lines 5-44
    
    """
    @f90wrap.runtime.register_class("test_scm.scalar")
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
            result = _test_scm.f90wrap_scalar_initialise()
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
                _test_scm.f90wrap_scalar_finalise(this=self._handle)
        
        @property
        def unit(self):
            """
            Element unit ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 14
            
            """
            return _test_scm.f90wrap_scalar__get__unit(self._handle)
        
        @unit.setter
        def unit(self, unit):
            _test_scm.f90wrap_scalar__set__unit(self._handle, unit)
        
        @property
        def comments(self):
            """
            Element comments ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 15
            
            """
            return _test_scm.f90wrap_scalar__get__comments(self._handle)
        
        @comments.setter
        def comments(self, comments):
            _test_scm.f90wrap_scalar__set__comments(self._handle, comments)
        
        @property
        def magnitude(self):
            """
            Element magnitude ftype=real(idp) pytype=float
            
            
            Defined at datatypes.fpp line 16
            
            """
            return _test_scm.f90wrap_scalar__get__magnitude(self._handle)
        
        @magnitude.setter
        def magnitude(self, magnitude):
            _test_scm.f90wrap_scalar__set__magnitude(self._handle, magnitude)
        
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
        
    
    @f90wrap.runtime.register_class("test_scm.datastore")
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
            result = _test_scm.f90wrap_datastore_initialise()
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
                _test_scm.f90wrap_datastore_finalise(this=self._handle)
        
        @property
        def unit(self):
            """
            Element unit ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 20
            
            """
            return _test_scm.f90wrap_datastore__get__unit(self._handle)
        
        @unit.setter
        def unit(self, unit):
            _test_scm.f90wrap_datastore__set__unit(self._handle, unit)
        
        @property
        def comments(self):
            """
            Element comments ftype=character(len = 50) pytype=str
            
            
            Defined at datatypes.fpp line 21
            
            """
            return _test_scm.f90wrap_datastore__get__comments(self._handle)
        
        @comments.setter
        def comments(self, comments):
            _test_scm.f90wrap_datastore__set__comments(self._handle, comments)
        
        @property
        def magnitude(self):
            """
            Element magnitude ftype=real(idp) pytype=float
            
            
            Defined at datatypes.fpp line 22
            
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
        _test_scm.f90wrap_init_datastore(dstore=self._handle, tsteps=tsteps, \
            dsunit=dsunit)
    
    @staticmethod
    def destroy_datastore(self):
        """
        destroy_datastore(self)
        
        
        Defined at datatypes.fpp lines 38-44
        
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
    @staticmethod
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
        _test_scm.f90wrap_set_datastore(dstore=self._handle, \
            dstore_magnitude=dstore_magnitude, dstore_unit=dstore_unit)
    
    _dt_array_initialisers = []
    

library = Library()

class Effective_Radiative_Forcing(f90wrap.runtime.FortranModule):
    """
    Module effective_radiative_forcing
    
    
    Defined at effective_radiative_forcing.fpp lines 5-18
    
    """
    @property
    def dat_effrf_total(self):
        """
        Element dat_effrf_total ftype=type(datastore) pytype=Datastore
        
        
        Defined at effective_radiative_forcing.fpp line 14
        
        """
        dat_effrf_total_handle = \
            _test_scm.f90wrap_effective_radiative_forcing__get__dat_effrf_total()
        if tuple(dat_effrf_total_handle) in self._objs:
            dat_effrf_total = self._objs[tuple(dat_effrf_total_handle)]
        else:
            dat_effrf_total = datatypes.datastore.from_handle(dat_effrf_total_handle)
            self._objs[tuple(dat_effrf_total_handle)] = dat_effrf_total
        return dat_effrf_total
    
    @dat_effrf_total.setter
    def dat_effrf_total(self, dat_effrf_total):
        dat_effrf_total = dat_effrf_total._handle
        \
            _test_scm.f90wrap_effective_radiative_forcing__set__dat_effrf_total(dat_effrf_total)
    
    def __str__(self):
        ret = ['<effective_radiative_forcing>{\n']
        ret.append('    dat_effrf_total : ')
        ret.append(repr(self.dat_effrf_total))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

effective_radiative_forcing = Effective_Radiative_Forcing()

class Temperature(f90wrap.runtime.FortranModule):
    """
    Module temperature
    
    
    Defined at temperature.fpp lines 5-81
    
    """
    @staticmethod
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
            _test_scm.f90wrap_temp_response_held_two_layer(effrf=effrf, tu=tu, tl=tl, \
            delta_t=delta_t)
        return temp_response_held_two_layer
    
    @property
    def dat_temperature_upper(self):
        """
        Element dat_temperature_upper ftype=type(datastore) pytype=Datastore
        
        
        Defined at temperature.fpp line 25
        
        """
        dat_temperature_upper_handle = \
            _test_scm.f90wrap_temperature__get__dat_temperature_upper()
        if tuple(dat_temperature_upper_handle) in self._objs:
            dat_temperature_upper = self._objs[tuple(dat_temperature_upper_handle)]
        else:
            dat_temperature_upper = \
                datatypes.datastore.from_handle(dat_temperature_upper_handle)
            self._objs[tuple(dat_temperature_upper_handle)] = dat_temperature_upper
        return dat_temperature_upper
    
    @dat_temperature_upper.setter
    def dat_temperature_upper(self, dat_temperature_upper):
        dat_temperature_upper = dat_temperature_upper._handle
        \
            _test_scm.f90wrap_temperature__set__dat_temperature_upper(dat_temperature_upper)
    
    @property
    def dat_temperature_lower(self):
        """
        Element dat_temperature_lower ftype=type(datastore) pytype=Datastore
        
        
        Defined at temperature.fpp line 26
        
        """
        dat_temperature_lower_handle = \
            _test_scm.f90wrap_temperature__get__dat_temperature_lower()
        if tuple(dat_temperature_lower_handle) in self._objs:
            dat_temperature_lower = self._objs[tuple(dat_temperature_lower_handle)]
        else:
            dat_temperature_lower = \
                datatypes.datastore.from_handle(dat_temperature_lower_handle)
            self._objs[tuple(dat_temperature_lower_handle)] = dat_temperature_lower
        return dat_temperature_lower
    
    @dat_temperature_lower.setter
    def dat_temperature_lower(self, dat_temperature_lower):
        dat_temperature_lower = dat_temperature_lower._handle
        \
            _test_scm.f90wrap_temperature__set__dat_temperature_lower(dat_temperature_lower)
    
    @property
    def dat_ocean_heat_uptake(self):
        """
        Element dat_ocean_heat_uptake ftype=type(datastore) pytype=Datastore
        
        
        Defined at temperature.fpp line 27
        
        """
        dat_ocean_heat_uptake_handle = \
            _test_scm.f90wrap_temperature__get__dat_ocean_heat_uptake()
        if tuple(dat_ocean_heat_uptake_handle) in self._objs:
            dat_ocean_heat_uptake = self._objs[tuple(dat_ocean_heat_uptake_handle)]
        else:
            dat_ocean_heat_uptake = \
                datatypes.datastore.from_handle(dat_ocean_heat_uptake_handle)
            self._objs[tuple(dat_ocean_heat_uptake_handle)] = dat_ocean_heat_uptake
        return dat_ocean_heat_uptake
    
    @dat_ocean_heat_uptake.setter
    def dat_ocean_heat_uptake(self, dat_ocean_heat_uptake):
        dat_ocean_heat_uptake = dat_ocean_heat_uptake._handle
        \
            _test_scm.f90wrap_temperature__set__dat_ocean_heat_uptake(dat_ocean_heat_uptake)
    
    @property
    def dat_rndt(self):
        """
        Element dat_rndt ftype=type(datastore) pytype=Datastore
        
        
        Defined at temperature.fpp line 28
        
        """
        dat_rndt_handle = _test_scm.f90wrap_temperature__get__dat_rndt()
        if tuple(dat_rndt_handle) in self._objs:
            dat_rndt = self._objs[tuple(dat_rndt_handle)]
        else:
            dat_rndt = datatypes.datastore.from_handle(dat_rndt_handle)
            self._objs[tuple(dat_rndt_handle)] = dat_rndt
        return dat_rndt
    
    @dat_rndt.setter
    def dat_rndt(self, dat_rndt):
        dat_rndt = dat_rndt._handle
        _test_scm.f90wrap_temperature__set__dat_rndt(dat_rndt)
    
    @property
    def du(self):
        """
        Element du ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 34
        
        """
        return _test_scm.f90wrap_temperature__get__du()
    
    @du.setter
    def du(self, du):
        _test_scm.f90wrap_temperature__set__du(du)
    
    @property
    def dl(self):
        """
        Element dl ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 35
        
        """
        return _test_scm.f90wrap_temperature__get__dl()
    
    @dl.setter
    def dl(self, dl):
        _test_scm.f90wrap_temperature__set__dl(dl)
    
    @property
    def lambda_0(self):
        """
        Element lambda_0 ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 36
        
        """
        return _test_scm.f90wrap_temperature__get__lambda_0()
    
    @lambda_0.setter
    def lambda_0(self, lambda_0):
        _test_scm.f90wrap_temperature__set__lambda_0(lambda_0)
    
    @property
    def b(self):
        """
        Element b ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 37
        
        """
        return _test_scm.f90wrap_temperature__get__b()
    
    @b.setter
    def b(self, b):
        _test_scm.f90wrap_temperature__set__b(b)
    
    @property
    def epsilon(self):
        """
        Element epsilon ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 38
        
        """
        return _test_scm.f90wrap_temperature__get__epsilon()
    
    @epsilon.setter
    def epsilon(self, epsilon):
        _test_scm.f90wrap_temperature__set__epsilon(epsilon)
    
    @property
    def eta(self):
        """
        Element eta ftype=real(idp) pytype=float
        
        
        Defined at temperature.fpp line 39
        
        """
        return _test_scm.f90wrap_temperature__get__eta()
    
    @eta.setter
    def eta(self, eta):
        _test_scm.f90wrap_temperature__set__eta(eta)
    
    def __str__(self):
        ret = ['<temperature>{\n']
        ret.append('    dat_temperature_upper : ')
        ret.append(repr(self.dat_temperature_upper))
        ret.append(',\n    dat_temperature_lower : ')
        ret.append(repr(self.dat_temperature_lower))
        ret.append(',\n    dat_ocean_heat_uptake : ')
        ret.append(repr(self.dat_ocean_heat_uptake))
        ret.append(',\n    dat_rndt : ')
        ret.append(repr(self.dat_rndt))
        ret.append(',\n    du : ')
        ret.append(repr(self.du))
        ret.append(',\n    dl : ')
        ret.append(repr(self.dl))
        ret.append(',\n    lambda_0 : ')
        ret.append(repr(self.lambda_0))
        ret.append(',\n    b : ')
        ret.append(repr(self.b))
        ret.append(',\n    epsilon : ')
        ret.append(repr(self.epsilon))
        ret.append(',\n    eta : ')
        ret.append(repr(self.eta))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

temperature = Temperature()

class Scm(f90wrap.runtime.FortranModule):
    """
    Module scm
    
    
    Defined at scm.fpp lines 5-110
    
    """
    @staticmethod
    def initialise_total_effective_radiative_forcing_driven(tsteps):
        """
        initialise_total_effective_radiative_forcing_driven(tsteps)
        
        
        Defined at scm.fpp lines 34-54
        
        Parameters
        ----------
        tsteps : int
        
        """
        \
            _test_scm.f90wrap_initialise_total_effective_radiative_forcing_driven(tsteps=tsteps)
    
    @staticmethod
    def step_total_radiative_forcing_driven(i):
        """
        step_total_radiative_forcing_driven(i)
        
        
        Defined at scm.fpp lines 56-94
        
        Parameters
        ----------
        i : int
        
        """
        _test_scm.f90wrap_step_total_radiative_forcing_driven(i=i)
    
    @staticmethod
    def run_total_radiative_forcing_driven():
        """
        run_total_radiative_forcing_driven()
        
        
        Defined at scm.fpp lines 96-110
        
        
        """
        _test_scm.f90wrap_run_total_radiative_forcing_driven()
    
    @property
    def timestep(self):
        """
        Element timestep ftype=type(scalar) pytype=Scalar
        
        
        Defined at scm.fpp line 18
        
        """
        timestep_handle = _test_scm.f90wrap_scm__get__timestep()
        if tuple(timestep_handle) in self._objs:
            timestep = self._objs[tuple(timestep_handle)]
        else:
            timestep = datatypes.scalar.from_handle(timestep_handle)
            self._objs[tuple(timestep_handle)] = timestep
        return timestep
    
    @timestep.setter
    def timestep(self, timestep):
        timestep = timestep._handle
        _test_scm.f90wrap_scm__set__timestep(timestep)
    
    def __str__(self):
        ret = ['<scm>{\n']
        ret.append('    timestep : ')
        ret.append(repr(self.timestep))
        ret.append('}')
        return ''.join(ret)
    
    _dt_array_initialisers = []
    

scm = Scm()

