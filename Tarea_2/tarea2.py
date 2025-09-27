from lista import *
#parasajero:: rut(str), nombre(str), categoria(str)

estructura.crear("pasajero", "rut nombre categoria")
p1 = pasajero("11.111.111-1", "Juan", "Elite Plus")
p2 = pasajero("22.222.222-2", "Ana", "Platinum")
p3 = pasajero("33.333.333-3", "Luis", "Gold")
p4 = pasajero("44.444.444-4", "Carla", "Flyer")
L = lista(p1, lista(p2, lista(p3, lista(p4, listaVacia))))
#esPasajeroValido: pasajero -> bool
#devuelve True si es un pasajero valido y False si no lo es
#ejemplo: esPasajeroValido(pasajero("22.142.429-7","Benjamin", "Gold"))
#ejemplo: esPasajeroValido(pasajero("12.345.678-9","Antonia",23))
def esPasajeroValido(p):
    return type(p) == pasajero and type(p.rut) == str and type(p.nombre) == str and type(p.categoria) == str and (p.categoria == "Elite Plus" or p.categoria == "Diamond" or p.categoria == "Platinum" or p.categoria == "Gold" or p.categoria == "Flyer" or p.categoria == "No Fidelizado")
assert esPasajeroValido(pasajero("22.142.429-7","Benjamin","Gold"))
assert not esPasajeroValido(pasajero("12.345.678-9","Antonia",23))


#listaCategoria(L,categoria):: lista(pasajero), str -> lista(pasajero)
#devuelve una lista de pasajeros que pertenecen a la categoria dada.
#ejemplo listarCategoria(L, "Gold") -> lista(valor=pasajero(rut='33.333.333-3', nombre='Juan', categoria='Elite Plus'),listaVacia) 
def listarCategoria(L, c):
    assert esLista(L)
    assert esPasajeroValido(cabeza(L)) or esListaVacia(cabeza(L))
    p = cabeza(L)
    if esListaVacia(L):
        return listaVacia
    if p.categoria == c:
        return lista(cabeza(L), listarCategoria(cola(L), c))
    else:
        return listarCategoria(cola(L), c)
assert listarCategoria(L,"No Fidelizado") == listaVacia
assert listarCategoria(L, "Gold") == lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'),siguiente=None)

#Concatenar(L1,L2):: lista(pasajero), lista(pasajero) -> lista(pasajero)
#esta funcion lo que hace es concatenar la lista L2 al final de L1, si L1 es vacia retorna L2 si L2 es vacia, retorna L1
        #concatenar(L,L)== lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=None))))))))`
def concatenar(L1,L2):
    assert esLista(L1)
    assert esPasajeroValido(cabeza(L1)) or esListaVacia(cabeza(L1))
    assert esLista(L2)
    assert esPasajeroValido(cabeza(L2)) or esListaVacia(cabeza(L2))
    if esListaVacia(L1):
        return L2
    else:
        return lista(cabeza(L1),concatenar(cola(L1),L2))
assert assert concatenar(L,L) == lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=None)))))))) 

#ordenarPasajeros(L):: lista(pasajero) ->lista(pasajero)
#devuelve una lista con los pasajeros ordenados según su prioridad
#ej: ordenarPasajeros(L) -> lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=None)))))
def ordenarPasajeros(L):
    assert esLista(L)
    assert esPasajeroValido(cabeza(L)) or esListaVacia(cabeza(L))
    resultado = concatenar(listarCategoria(L,"Elite Plus"),concatenar(listarCategoria(L,"Diamond"),concatenar(listarCategoria(L,"Platinum"),concatenar(listarCategoria(L,"Gold"),concatenar(listarCategoria(L,"Flyer"),concatenar(listarCategoria(L,"Flyer"),listaVacia))))))
    return resultado
assert ordenarPasajeros(L) == lista(valor=pasajero(rut='11.111.111-1', nombre='Juan', categoria='Elite Plus'), siguiente=lista(valor=pasajero(rut='22.222.222-2', nombre='Ana', categoria='Platinum'), siguiente=lista(valor=pasajero(rut='33.333.333-3', nombre='Luis', categoria='Gold'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=lista(valor=pasajero(rut='44.444.444-4', nombre='Carla', categoria='Flyer'), siguiente=None))))) 


