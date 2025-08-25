from math import *
#sol1 num num num -> num
# esta funcion calcula una cuadratica con coef a b c
# ejemplo sol1(1,0,0) return 0
def sol1(a,b,c):
    sol1 = ((-b+sqrt(b**2-4*a*c))/2*a)
    return sol1
assert sol1(1,1,-6) == 2


#sol1 num num num -> num
# esta funcion calcula una cuadratica con coef a b c
# ejemplo sol2(1,1,-6) return 3
def sol2(a,b,c):
    sol2 = ((-b-sqrt(b**2-4*a*c))/2*a)
    return sol2
assert sol2(1,1,-6) == -3


