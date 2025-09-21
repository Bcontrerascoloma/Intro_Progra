from lista import *
import estructura as e
#ListaTeclado :: None -> lista(int)
#Crea una lista con valores leidos desde el teclado hasta que recibamos un entero <= 0
def listaTeclado():
    valor = int(input("valor?"))
    if valor <= 0:
        return listaVacia
    return lista(valor, listaTeclado())
#listaTeclado()

#listaTeclado2 :: None -> lista(int)
#misma funcion que listaTeclado, pero los valores ahora los encolamos por el inicio
def listaTeclado2(L=listaVacia):
    valor = int(input("valor?"))
    if valor <= 0:
        return L
    return listaTeclado2(lista(valor,L))
listaTeclado2()



#estudiante :: nombre(str), helado(str), nota(float)
e.crear("estudiante", "nombre helado nota")
estudiante_1 = estudiante("Sofía", "fresa", 8.5)
estudiante_2 = estudiante("Andrés", "pistacho", 7.0)
estudiante_3 = estudiante("Paula", "chocolate", 9.2)
estudiante_4 = estudiante("Luis", "vainilla", 6.8)
estudiante_5 = estudiante("Elena", "menta", 5.5)
estudiante_6 = estudiante("Carlos", "ron pasas", 9.8)
estudiante_7 = estudiante("Javier", "café", 7.9)
estudiante_8 = estudiante("Marina", "limón", 6.0)
estudiante_9 = estudiante("Diego", "nuez", 8.1)
estudiante_10 = estudiante("Valentina", "coco", 10.0)
