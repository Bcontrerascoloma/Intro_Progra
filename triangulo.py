from math import *
#perimetro num num num -> num
#esta funcion calcula el perimetro de un triangulo de lados a,b,c
#ejemplo perimetro(2,3,5) retorna 10
def perimetro(a,b,c):
    return a+b+c
#Test 
assert perimetro(2,3,5) == 10

#area: num num num -> num
#Esta funcion toma los lados a,b,c de un triangulo y calcula su area
#Ejemplo: area(3,4,5) retorna 3
def area(a,b,c):
    semi_perimetro = perimetro(a,b,c)/2
    area = sqrt(semi_perimetro*(semi_perimetro-a)*(semi_perimetro-b)*(semi_perimetro-c))
    return area
#Test a
assert area(3,4,5) == 6
