module effective_radiative_forcing

    use datatypes, only: datastore

    implicit none
    private
    public :: dat_effrf_total

    ! have to make things target so that we can get pointers to them
    type(datastore), target, save :: dat_effrf_total
    ! Could I skip the save keyword like below? My initial reading of https://stackoverflow.com/questions/2893097/fortran-save-statement suggests no because this module will go in and out of scope but I could be missing something...
    ! type(datastore), target :: dat_effrf_total

contains

end module effective_radiative_forcing
