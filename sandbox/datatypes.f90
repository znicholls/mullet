module datatypes

    use parameters, only: idp, isp

    implicit none
    private
    public :: datastore, init_datastore, destroy_datastore, scalar

    type scalar
        character(len = 50) :: unit
        character(len = 50) :: comments
        real(idp) :: magnitude
    end type scalar

    type datastore
        character(len = 50) :: unit
        character(len = 50) :: comments
        real(idp), dimension(:), allocatable :: magnitude
    end type datastore

contains

    subroutine init_datastore(dstore, tsteps, dsunit)

        type(datastore), intent(inout) :: dstore
        integer, intent(in) :: tsteps
        character(len = 50), intent(in) :: dsunit

        allocate(dstore%magnitude(tsteps))
        dstore%unit = dsunit

    end subroutine init_datastore

    subroutine destroy_datastore(dstore)

        type(datastore), intent(inout) :: dstore

        if (allocated(dstore%magnitude)) deallocate(dstore%magnitude)

    end subroutine destroy_datastore

end module datatypes
