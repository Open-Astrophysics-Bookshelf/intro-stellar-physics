program machar
    use iso_fortran_env
    real(real64), parameter :: one = 1.0_real64
    integer(int64), parameter :: ione = 1
    write(*,'(a16,"[",i5,",",i5,"]")') 'exponent = ',minexponent(one),maxexponent(one)
    write(*,'(a16,i2)') 'digits = ',digits(one)
    write(*,'(a16,"[",es12.4e3,",",es12.4e3,"]")') '[tiny, huge] = ',tiny(one),huge(one)
    write(*,'(a16,i2)') 'precision = ',precision(one)
    write(*,'(a16,es10.4)') 'epsilon = ',epsilon(one)
    write(*,'(/,a,/,16("="))') 'integers'
    write(*,'(a16,i2)') 'digits = ',digits(ione)
    write(*,'(a16,i20)') 'huge = ',huge(ione)
end program machar
