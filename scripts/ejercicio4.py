from lista import *
#contar_votos(opcion,votos)
#cuenta cunatas veces se voto por opcion en votos
#Ej: contar_votos("Mati", lista("Mati", lista("Marla", lista("Mati", listaVacia)))) -> 2
#Ej: contar_votos("Marla", lista("Mati", lista("Marla", lista("Mati", listaVacia)))) -> 1
def contar_votos(opcion,lista):
    if esListaVacia(lista):
        return 0
    else:
        if cabeza(lista) == opcion:
            return 1 + contar_votos(opcion,cola(lista))
        else:
            return contar_votos(opcion,cola(lista))
assert contar_votos("Mati", lista("Mati", lista("Marla", lista("Mati", listaVacia)))) == 2
assert contar_votos("Marla", lista("Mati", lista("Marla", lista("Mati", listaVacia)))) == 1

# ganador:: lista -> None
# imprime la opcion ganadora y su porcentaje de votación
def ganador(votos):
    votosMarla = contar_votos("Marla",votos)
    votosMati = contar_votos("Mati",votos)
    vt = votosMarla + votosMati
    if votosMati == votosMarla:
        print("Mati y Marla empataron")
    elif votosMarla < votosMati:
        porcentaje = (votosMati/vt)*100
        print("La opción Mati ganó con un ",round(porcentaje,2), "% de los votos")
    else:
        porcentaje = (votosMarla/vt)*100
        print("La opción Mati ganó con un ",round(porcentaje,2), "% de los votos")
v = lista("Mati", lista("Marla", lista("Mati", lista("Mati", lista("Marla", lista("Mati", listaVacia))))))
ganador(v)
#Este procedimiento imprime "La opción Mati ganó con un  66.67 % de los votos"

