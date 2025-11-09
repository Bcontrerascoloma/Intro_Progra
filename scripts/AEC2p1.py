import estructura
from lista import *

# Disfraz: nombre(str) cantidad(int) talla(str)
estructura.crear('Disfraz','nombre talla cantidad')
LD = lista(Disfraz('fantasmita','XS',5),lista(Disfraz('fantasmita','S',0),lista(Disfraz('pirate','S',3),lista(Disfraz('esqueleto','M',5), lista(Disfraz('momia','M',0),lista(Disfraz('fantasmita','L',4), lista(Disfraz('momia','L',1),lista(Disfraz('esqueleto','XL',1),listaVacia))))))))

def sinStock(Ld):
    assert type(Ld) == lista
#   assert esLista(Ld)
    if esListaVacia(Ld):
        return listaVacia
    else:
        disfraz1 = cabeza(Ld)
        if disfraz1.cantidad == 0:
            return lista(disfraz1,sinStock(cola(Ld)))
        else:
            return sinStock(cola(Ld))

def contar(Ld,t):
    assert esLista(Ld)
    assert type(t) = str
    if esListaVacia(Ld):
        return 0
    else:
        disfraz1 = cabeza(Ld)
        if disfraz1.talla == t:
            return 1 + contar(cola(Ld),t)
        else:
            return contar(cola(Ld),t)

def filtrarTalla(Ld,t):
    assert esLista(Ld)
    assert type(t) = str
    if esListaVacia(Ld):
        return listaVacia
    else:
        disfraz1 = cabeza(Ld)
        if disfraz1.talla == t:
            return lista(disfraz1,filtrarTalla(cola(Ld),t))
        else:
            return filtrarTalla(cola(Ld),t)

def incrementar(Ld,nombre):
    if Ld == listaVacia: 
        return listaVacia 
    else: 
        if cabeza(Ld).nombre == nombre: 
            nuevo == disfraz(cabeza(ld).nombre, cabeza(ld).talla, cabeza(ld).cantidad +1) 
            return lista(nuevo, incrementar(cola(ld), nombre)) 
        else: 
            return lista(cabeza(ld), incrementar(cola(ld), nombre))
