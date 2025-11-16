from tareaA import *
lista_animales=[]
cargarAnimales("animales.txt",lista_animales)
agregarAvistamientos("avistamientos.txt",lista_animales)
print(zonaMasProbable("zorro",23,lista_animales))
