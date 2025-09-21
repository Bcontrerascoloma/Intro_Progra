#Aux5
#1C1B2A
from lista import *

import estructura
from lista import *
estructura.crear("Punto","x y")

p1 = Punto(1,2)
#print(p1.x)
#print(p1.y)
from lista import *
l1  = lista(3,lista(2,lista(6,lista(8,lista(10,None)))))
#print(cola(l1))

def printearLista(l):
    if esListaVacia(l):
        return None
    else:
        print(cabeza(l))
        printearLista(cola(l))
#printearLista(l1)
def buscarEnLista(l,x):
    if esListaVacia(l):
        return False
    else:
        if cabeza(l) ==x:
            return True
        else:
            return buscarEnLista(cola(l),x)
assert not buscarEnLista(l1,90)
assert buscarEnLista(l1,2)

def invertir(l,aux=None):
    if esListaVacia(l):
        return aux
    else: 
        #tomar su primer elemento
        elemento = cabeza(l)
        aux = lista(elemento,aux)
        return invertir(cola(l),aux)
#printearLista(invertir(l1))
################## AUX 5 ################################

#distancia Punto, Punto -> int
#calcula la distancia entre p1 y p2 
# ej distancia(Punto(1,2),Punto(1,2)) -> 0
def distancia(p1,p2):
    x1 = p1.x
    x2 = p2.x
    y1 = p1.y
    y2 = p2.y
    return abs(x1-x2)+abs(y1-y2)
assert distancia(Punto(5,5),Punto(1,1)) == 8

#agregar Punto lista -> lista
#se agrega el Punto a la ruta
#ej agregar(Punto(1,1), None) -> lista(Punto(1,1), None)
def agregar(p,ruta):
    if esListaVacia(ruta):
        return lista(p,None)
    else:
        return lista(cabeza(ruta),agregar(p, cola(ruta)))
assert  agregar(Punto(1,1), None) == lista(Punto(1,1), None)

# largo: lista -> int
# retorna la cantidad de puntos de una lista
#
def largo(ruta):
    if esListaVacia(ruta):
        return 0
    else:
        return 1 + largo(cola(ruta))
assert largo(lista(Punto(1,1),lista(Punto(9,99),None))) == 2
assert largo(None) == 0



#quitarPunto Punto lista -> lista
#quita el punto p a la ruta
#ej quitarPunto(Punto(1,1),lista(Punto(1,1),None)) -> None
def quitarpunto(p,ruta):
    if esListaVacia(ruta)
        return listaVacia
    else:
        primerElemento = cabeza(ruta)
        if primerElemento == p
            return cola(ruta)
        else:
            return lista(primerElemento,quitarpunto(p,cola(ruta)))

#masCercano Punto, lista -> Punto
#retorna el punto mas cerncano a p
#ej: masCercano(Punto(1,2),lista(Punto(2,2),None)) -> Punto(2,2)
def masCercano(p,ruta,pto=None,d=None):
    if esListaVacia(ruta):
        return pto
    else:
        if pto== None and d == None: #Caso en el que no he revisado mas puntos
            #Asumo que el primero es el mas cercano
            return masCercano(p, cola(ruta) , cabeza(ruta), distancia(p,cabeza(ruta)))
        else: 
            puntoActual = cabeza(ruta)
            dist =distancia(p,puntoActual)
            if dist<d:
                #actualizo el punto mas cercano
                return masCercano(p,cola(ruta),puntoActual,distancia)
            else:
                return masCercano(p,cola(ruta),pto,d)






