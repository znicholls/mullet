module scm

    use datatypes, only: scalar
    use parameters, only: idp, isp

    implicit none
    private
    public :: timestep, &
              initialise_total_effective_radiative_forcing_driven, &
              step_total_radiative_forcing_driven, &
              run_total_radiative_forcing_driven

    ! not sure if target and save are needed here...
    type(scalar), target, save :: timestep
    ! , &
    !           run_total_radiative_forcing_driven

contains

    subroutine intialise_defaults_core_and_units()

        use utils, only: initialise_utils, one_year

        call initialise_utils()

        timestep = one_year

    end subroutine intialise_defaults_core_and_units

    subroutine initialise_total_effective_radiative_forcing_driven(tsteps)

        use effective_radiative_forcing, only: dat_effrf_total
        use temperature, only: dat_temperature_upper, &
                               dat_temperature_lower, &
                               ! dat_ocean_heat_uptake, &
                               dat_rndt
        use datatypes, only: init_datastore

        integer, intent(in) :: tsteps

        call intialise_defaults_core_and_units()
        ! the order of these two lines matters for whether the units are set
        ! correctly or not, see the comments in test.py
        call init_datastore(dat_temperature_upper, tsteps, "K")
        call init_datastore(dat_temperature_lower, tsteps, "K")
        ! call init_datastore(dat_ocean_heat_uptake, tsteps, "K")
        call init_datastore(dat_rndt, tsteps, "W/m^2")
        call init_datastore(dat_effrf_total, tsteps, "W/m^2")

    end subroutine initialise_total_effective_radiative_forcing_driven

    subroutine step_total_radiative_forcing_driven(i)

        ! Run in a total radiative forcing only driven mode

        use effective_radiative_forcing, only: dat_effrf_total
        use temperature, only: dat_temperature_upper, &
                               dat_temperature_lower, &
                               ! dat_ocean_heat_uptake, &
                               dat_rndt, &
                               temp_response_held_two_layer
        use utils, only: water_density, water_heat_capacity

        integer, intent(in) :: i
        real(idp) :: calc_result(3)

        if (water_density%unit /= "kg m^-3") then
            print *, "Wrong unit for water density"  ! wrong units, must be better way to handle this
        endif
        if (water_heat_capacity%unit /= "J K^-1 kg^-1") then
            print *, "Wrong unit for water heat capacity"  ! wrong units, must be better way to handle this
        endif

        if (i.eq.1) then
            dat_temperature_upper%magnitude(i) = 0
            dat_temperature_lower%magnitude(i) = 0
            dat_rndt%magnitude(i) = 0
        else
            calc_result = temp_response_held_two_layer( &
                EFFRF=dat_effrf_total%magnitude(i - 1), &
                TU=dat_temperature_upper%magnitude(i - 1), &
                TL=dat_temperature_lower%magnitude(i - 1), &
                delta_t=timestep%magnitude &
            )
            dat_temperature_upper%magnitude(i) = calc_result(1)
            dat_temperature_lower%magnitude(i) = calc_result(2)
            dat_rndt%magnitude(i) = calc_result(3)
        endif

    end subroutine step_total_radiative_forcing_driven

    subroutine run_total_radiative_forcing_driven()

        ! Run in a total radiative forcing only driven mode

        use effective_radiative_forcing, only: dat_effrf_total

        integer :: i, n

        n = size(dat_effrf_total%magnitude)

        do i = 1, n
            call step_total_radiative_forcing_driven(i)
        enddo

    end subroutine run_total_radiative_forcing_driven

end module scm
