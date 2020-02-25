module parameters

    implicit none
    private
    public :: idp, isp

    integer, parameter :: idp=kind(1d0)  ! double precision, np.float64 equivalent
    integer, parameter :: isp=kind(1e0)  ! single precision, np.float32 equivalent

contains

end module parameters
