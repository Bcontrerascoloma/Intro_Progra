import estructura
import math
#Fraccion: numerador(int) denominador(int)
estructura.crear("Fraccion", "numerador denominador")

Frac1 = Fraccion(5,8)
Frac2 = Fraccion(1,3)
Frac3 = Fraccion(3,12)
Frac4 = Fraccion(1,4)

#fracToStr(F):: Fraccion -> str
def fracToStr(F):
    n = str(F.numerador)
    d = str(F.denominador)
    texto = (f"{n}/{d}")
    return(texto)
assert fracToStr(Frac1) == "5/8"
#simplificar(F):: Fraccion -> Fraccion
def simplificar(F):
    m= math.gcd(F.numerador, F.denominador)
    Fnueva= Fraccion(F.numerador/m,F.denominador/m)
    return Fnueva
assert simplificar(Frac3) == Fraccion(1,4)
def restar(F1,F2):
    Fn= Fraccion((F2.denominador*F1.numerador)-(F1.denominador*F2.numerador),F1.denominador*F2.denominador)
    return Fn
assert restar(Frac1,Frac2) == Fraccion(7,24)

def multiplicar(F1,F2):
    Fn= Fraccion((F2.numerador*F1.numerador),F1.denominador*F2.denominador)
    return Fn
assert multiplicar(Frac1,Frac2) == Fraccion(5,24)

def dividir(F1,F2):
    Fn= Fraccion((F2.denominador*F1.numerador),F1.denominador*F2.numerador)
    return Fn
assert dividir(Frac1,Frac2) == Fraccion(15,8)
def iguales(F1,F2):
    return (F1.numerador*F2.denominador == F2.numerador*F1.denominador)
assert iguales(Frac3,Frac4) == True
def mayor(F1,F2):
    if iguales(F1,F2):
        return F1
    elif (F1.numerador/F1.denominador) > (F2.numerador/F2.denominador):
        return F1
    else:
        return F2
assert mayor(Frac3,Frac4) == Fraccion(3,12)
assert mayor(Frac1,Frac2) == Fraccion(5,8)
