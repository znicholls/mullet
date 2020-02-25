module library

    use parameters, only: idp, isp

    implicit none
    private
    ! public ::

contains

    subroutine set_datastore(dstore, dstore_magnitude, dstore_unit)

        use datatypes, only: datastore

        type(datastore), intent(inout) :: dstore
        real(kind=idp), intent(in) :: dstore_magnitude
        character(len = 50), intent(in) :: dstore_unit

        dstore%magnitude = dstore_magnitude
        dstore%unit = dstore_unit

    end subroutine set_datastore

end module library
