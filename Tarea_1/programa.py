from tarea1 import *
# input de los puntos de la cuadricula cunado se ingrese 0 se corta
# # componer la ruta por crcania 

# (1) generar la ruta, solicitando por teclado los puntos a visitar (hasta
# que se ingrese 0); (2) determinar en cada paso cuál es el siguiente punto al que debe desplazarse el
# repartidor (priorizando elegir el más cercano, sin repeticiones); (3) mostrar en pantalla el recorrido,
# indicando claramente cuál es el primer punto de la ruta, los puntos intermedios y el punto final; y (4)
# mostrar la distancia total que recorrió el repartidor al final del proceso. Como guía, puede utilizar el
# siguiente modelo de diálogo que cumple los requisitos mencionados anteriormente:
origen = 1010
ordenar(origen,leer_teclado())