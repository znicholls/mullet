module temperature

    use datatypes, only: datastore
    use parameters, only: idp, isp

    implicit none
    private
    public :: dat_temperature_upper, &
              dat_temperature_lower, &
              dat_ocean_heat_uptake, &
              dat_rndt, &
              DU, &
              DL, &
              lambda_0, &
              b, &
              epsilon, &
              eta, &
              temp_response_held_two_layer

    ! have to make things target so that we can get pointers to them
    type(datastore), target, save :: dat_temperature_upper
    type(datastore), target, save :: dat_temperature_lower
    type(datastore), target, save :: dat_ocean_heat_uptake
    type(datastore), target, save :: dat_rndt
    ! Could I skip the save keyword like below? My initial reading of https://stackoverflow.com/questions/2893097/fortran-save-statement suggests no because this module will go in and out of scope but I could be missing something...
    ! type(datastore), target :: dat_rf_total

    ! I should probably rename this module to temperature_held_two_layer given
    ! these variables
    real(idp), target, save :: DU = 50.0_idp  ! depth of upper ocean layer (m)
    real(idp), target, save :: DL = 1200.0_idp  ! depth of lower ocean layer (m)
    real(idp), target, save :: lambda_0 = -3.74_idp / 3.0_idp  ! climate feedback parameter for T_upper=0 (W m^-2 K^-1)
    real(idp), target, save :: b = 0.0_idp ! state dependent feedback term (W m^-2 K^-2)
    real(idp), target, save :: epsilon = 1.0_idp  ! efficacy factor for ocean heat uptake (dimensionless)
    real(idp), target, save :: eta = 0.8_idp  ! heat transport efficiency (W m^-2 K^-1)

contains

    pure function temp_response_held_two_layer(EFFRF, TU, TL, delta_t)

        ! Calculate temperature response from input emissions

        use utils, only: water_density, water_heat_capacity

        real(idp), intent(in) :: EFFRF, TU, TL, delta_t
        real(idp) :: tu_next, tl_next, rndt_next, exchange, CU, CL
        real(idp) :: temp_response_held_two_layer(3)

        CU = water_density%magnitude * water_heat_capacity%magnitude * DU
        CL = water_density%magnitude * water_heat_capacity%magnitude * DL

        exchange = eta * (TU - TL)

        tu_next = ( &
            TU &
            + delta_t &
            * ( &
                EFFRF &
                + (lambda_0 + b * TU) * TU &
                - (epsilon * exchange) &
            ) &
            / CU &
        )

        tl_next = ( &
            TL &
            + delta_t * exchange / CU &
        )

        rndt_next = ( &
            CU * (tu_next - TU) &
            + CL * (tl_next - TL) &
        ) / delta_t

        temp_response_held_two_layer = [tu_next, tl_next, rndt_next]

    end function

end module temperature
