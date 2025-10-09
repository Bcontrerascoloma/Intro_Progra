import estructura
from lista import *
from scripts import lista
#triangulo: a(num), b(num), c(num)
estructura.crear("triangulo", "a b c")
# ejemplos de triángulos
T1 = triangulo(5, 5, 3) # isósceles
T2 = triangulo(7, 5, 4) # escaleno
T3 = triangulo(6, 6, 6) # equilátero
T4 = triangulo(3, 5, 4) # escaleno
T5 = triangulo(1, 3, 1) # no es triangulo
# lista de triángulos
LT = lista(T1, lista(T2, lista(T3, lista(T4, lista(T5, listaVacia)))))

#soloIso: lista(triangulo) -> lista(triangulo)
#entrega una lista solo con triángulos isoceles
#soloIso(LT) -> lista(T1, listaVacia)
def soloIso(L):
    if L == listaVacia
        return listaVacia
    else:
        if type(cabeza(L)) == 2:
            return lista(cabeza(L),soloIso(cola(L))
        else:
            return soloIso(cola(L))
assert soloIso(LT)==lista(T1, listaVacia)


def soloIso(L):

