program machar
    use iso_fortran_env
    real(real64), parameter :: one = 1.0_real64
    write(*,'(a16,"[",i5,",",i5,"]")') 'exponent = ',minexponent(one),maxexponent(one)
    write(*,'(a16,"[",es12.4e3,",",es12.4e3,"]")') '[tiny, huge] = ',tiny(one),huge(one)
    write(*,'(a16,i2)') 'precision = ',precision(one)
    write(*,'(a16,es10.4)') 'epsilon = ',epsilon(one)
end program machar
