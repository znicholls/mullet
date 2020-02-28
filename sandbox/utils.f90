module utils

    use parameters, only: idp, isp
    use datatypes, only: scalar

    implicit none
    private
    public :: initialise_utils, &
              one_year, water_density, water_heat_capacity

    type(scalar) :: one_year, water_density, water_heat_capacity

contains

    subroutine initialise_utils()

        one_year%magnitude = 365.0_idp * 24.0_idp * 60.0_idp * 60.0_idp
        one_year%unit = "s"

        water_density%magnitude = 1000.0_idp
        water_density%unit = "kg m^-3"

        water_heat_capacity%magnitude = 4181.0_idp
        water_heat_capacity%unit = "J K^-1 kg^-1"

    end subroutine initialise_utils

end module utils


