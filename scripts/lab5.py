import estructura 
from lista import *

def filtro(L,predicado):
    assert esLista(L)
    if L == listaVacia:
        return listaVacia
    if predicado(cabeza(L)):
        return lista(cabeza(L),filtro(cola(L),predicado))
    return filtro(cola(L),predicado)

estructura.crear("animal","nombre especie peso")
L = lista( animal("Toby", "Perro", 12),lista( animal("Mimi", "Gato", 5),lista(animal("Rex", "Perro", 20),listaVacia)))
#animales_especie(L,especie):: lista(animal) -> lista(animal)
#retorna una lista con todos los animales que tengan la especie del parametro especie
#ejemplo animales_especie(L,"Perro") -> lista(animal("Toby","Perro",12), lista(animal("Rex","Perro",20), listaVacia))
def animales_especie(L,especie):
    assert esLista(L)
    assert type(especie) == str
    if esListaVacia(L):
        return
    if (cabeza(L)).especie== especie:
        return lista(cabeza(L),animales_especie(cola(L),especie))
    else:
        return animales_especie(cola(L),especie)
assert animales_especie(L,"Perro") == lista(animal("Toby","Perro",12), lista(animal("Rex","Perro",20), listaVacia))

#animales_pesados(L,peso_min):: lista(animales) -> lista(animales)
#retorna animales con peso mayor que peso_min
#ej animales_pesados(L,10) == lista(animal("Toby","Perro",12), lista(animal("Rex","Perro",20), listaVacia))
def animales_pesados(L,peso_min):
    assert esLista(L)
    assert type(peso_min)== int
    return filtro(L, lambda x: x.peso> peso_min)
assert animales_pesados(L,10) == lista(animal("Toby","Perro",12), lista(animal("Rex","Perro",20), listaVacia))