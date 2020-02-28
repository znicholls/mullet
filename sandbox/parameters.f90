module parameters

    implicit none
    private
    public :: idp, isp

    integer, parameter :: idp=kind(0.d0)  ! double precision
    integer, parameter :: isp=kind(0.e0)  ! single precision

contains

end module parameters
