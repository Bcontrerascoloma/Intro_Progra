#TAREA 1 INTRO A LA PROGRA BENJAMIN CONTRERAS-COLOMA 22.142.424-7


#funcion distancia
#distancia(punto1,punto2):: int int -> int
#Calcula la distancia de Manhattan entre los puntos punto1 y punto2
#Ejemplo distancia(4030,9070) return 90

def distancia(punto1,punto2):
    x1 = punto1%100
    y1 = punto1//100
    x2 = punto2%100
    y2 = punto2//100  
    d = abs(x2 - x1) + abs(y2-y1)
    return d

#test
assert distancia(4030,9070) == 90
assert distancia(1010, 1010) == 0 # misma coordenada


#funcion agregar
#agregar(punto,ruta):: int int -> int
#agrega el punto a la ruta dada
#ejemplo: agregar(1234,50607080) return 506070801234

def agregar(punto,ruta):
    n = ruta * 10**4  #Esto lo hago para poder mover en 4 espacios hacia la izquierda la ruta original y llenar con 0
    ruta_nueva = n + punto
    return ruta_nueva

#test
assert agregar(1234,50607080) == 506070801234
assert agregar(9999, 0) == 9999                  # agregarmos a ruta vacía deberia retornar solo el punto 
assert agregar(2020, 1010) == 10102020           # ruta de 1 punto


#funcion primerPunto
#primerPunto(ruta) :: int -> int
#Esta funcion retorna el primer punto de una ruta dada.
#ejemplo: primerPunto(102030405060) return 5060

def primerPunto(ruta):
    return (ruta%(10**4))

#test
assert primerPunto(102030405060) == 5060
assert primerPunto(9999) == 9999                 # ruta con un punto
assert primerPunto(12345678) == 5678             # ruta con dos puntos


# funcion restoRuta
#restoRuta(ruta):: int -> int
#esta funcion retorna la ruta sin el primer punto
#ejemplo: restoRuta(102030405060) return 10203040

def restoRuta(ruta):
    return (ruta//(10**4)) # con la division parte entera lo que hacemos es "quitar" las n cifras correspondientes a la potencia de base 10

#test
assert restoRuta(102030405060) == 10203040
assert restoRuta(9999) == 0                      # ruta de un solo punto → vacío
assert restoRuta(12345678) == 1234               # ruta con dos puntos


#funcion largo
#largo(ruta):: int -> int
#retorna la cantidad de puntos en la ruta dada 
#ejemplo largo(10203040) return 2

def largo(ruta):
    if ruta == 0:
        return 0
    else:
        #return 1 + largo(restoRuta(ruta))
        return 1 + largo(ruta//(10**4))

#test
assert largo(10203040) == 2
assert largo(9999) == 1                          # ruta con un punto
assert largo(0) == 0


#funcion quitarPunto(punto,ruta):: int int -> int
#esta funcion retorna la ruta eliminando el punto dado 
#ejemplo quitarPunto(10203040,3040) return 1020
#ejemplo quitarPunto(3036,3036) return 0

def quitarPunto(punto,ruta):
    if ruta ==0:
        return 0
#pensando las coordenadas como trenes
    if primerPunto(ruta) == punto: #caso en que queramos eliminar el primer punto
        return restoRuta(ruta)
    else:   
        sigamosBuscando = quitarPunto(punto,restoRuta(ruta)) 
#ejecutamos la funcion de forma recursiva, pues como el primer punto no era el punto a eliminar seguimos buscando en el resto de la ruta hasta que lleguemos al caso base de que punto == primerPunto
        return agregar(primerPunto(ruta), sigamosBuscando) 
#como en sigamosBuscando ya conseguimos eliminar el punto, simplemente nos queda agregar nuevamente el primer punto a la ruta, pues es este el primer punto ya que no era el punto a eliminar y debemos conservar el orden

#test
assert quitarPunto(3036,3036) == 0
assert quitarPunto(1010, 10102020) == 2020       # elimina el primero
assert quitarPunto(2020, 10102020) == 1010       # elimina el último
assert quitarPunto(9999, 10102020) == 10102020   # punto no está en la ruta → se conserva


#funcion masCercano
#quitarPunto(punto,ruta) :: int int -> int
#esta funcion retorna el punto mas cercano al punto del parametro
#ejemplo: quitarPunto(1010,1010505060602020) retun 1010

def masCercano(punto,ruta):
#que debemos hacer? comparar la distancia de cada punto de la ruta y devolver la menor
    resto = restoRuta(ruta)
    pp = primerPunto(ruta)
    if resto == 0:
        return pp
    if distancia(punto, pp) <= distancia(punto,(masCercano(punto,resto))):
        return pp
    else:
        return masCercano(punto,resto)
    

#test
assert masCercano(1010, 10102020) == 1010
assert masCercano(1515, 10102020) == 1010 or 2020 # empate de distancias
assert masCercano(9090, 101020203040) == 3040    # punto más cercano al extremo
assert masCercano(5678, 5678) == 5678            # ruta de un solo punto


#FUNNCIONES AUXILIARES USADAS PARA EL PROGRAMA, NO SABIA SI PONERLAS EN ESTE O EN PROGRAMA.PY 
#ASUMO QUE DA IGUAL

#LEER TECLADO
#leer_teclado():: none -> int#funcion auxiliar
#Esta función lo que hace es tomar los inputs del teclado y convertirlos en solo numero entero donde se guarden las coordenadas
#cuando le ingresamos int(0) la funcion termina y nos retorna la ruta
#ejemplo leer_teclado() return 10109090 (creo que no tiene mucho sentido hacer un ejemplo pero ante la duda lo hago)

def leer_teclado(): 
    a = int(input("Ingrese un punto: "))
    if a == 0:
        return 0
    else:
        ruta = agregar(a,leer_teclado())
        return ruta
    

#DELIVERY (MAIN)    
#delivery(posicion,ruta,avance,distanciaRecorrida):: int int int int -> none
#Esta función toma la posicion de origen y calcula el punto siguiente de la ruta, el mas cercano y sigue asi hasta cuando ya recorrio todos los puntos
#En este caso como el repartidor siempre parte desde el origen posicion parte en 1010 como var por omision 
#La ruta es extraida del input del usuario con leer_teclado, avance para lo que nos sirve es para controlar que mensaje imprimir
#y en la var distancia recorrida guardo la suma de las distancias entre los tramos recorridos 

def delivery(posicion=1010,ruta=leer_teclado(),avance=1,distanciaRecorrida=0):
    if ruta == 0:
        print("La distancia recorrida fue: ", distanciaRecorrida)
        return
    proxPaso = masCercano(posicion,ruta)
    distanciaPaso = distancia(posicion,proxPaso) #aqui lo que hacemos es es ver cuanto recorremos en cada paso
    if avance == 1:
        print("El primer punto a visitar debe ser el ", proxPaso)
    elif largo(ruta) == 1:
        print("Finalmente se debe dirigir al punto ", proxPaso)
    else: 
        print("Luego debe dirigirse al punto ", proxPaso)
    return delivery(proxPaso,quitarPunto(proxPaso,ruta),avance +1, distanciaRecorrida + distanciaPaso)
#Comentario: al poner la funcion leer_teclado como var por omision tuve el problema que la funcion se me ejecutaba sin llamarla :/ ojala no descuente tanto