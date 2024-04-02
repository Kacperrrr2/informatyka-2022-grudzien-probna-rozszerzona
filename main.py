def ile_rozkladow_golsbacha(liczba):
     ile_rozkladow=0
     for i in range(2,liczba//2+1):
         if  czy_pierwsza(liczba-i) and czy_pierwsza(i):
             ile_rozkladow=ile_rozkladow+1
     return ile_rozkladow


def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True



print(f'{ile_rozkladow_golsbacha(22)}')