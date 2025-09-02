#HACER LOS TEST

#espectadores: int -> int


#Calcula la cantidad de espectadores a partir de precioEntrada
precioEntrada = int(input('Cuanto vale la entrada? '))
def espectadores(precioEntrada):
    return 120 + (5000-precioEntrada)*15/500
#ganancias: int -> int
#Calcula las ganancias del cine, la diferencia entre sus ingresos y sus gastos 
def ganancias(precioEntrada):
    return (ingresos(precioEntrada) - gastos(precioEntrada))
#ingresos: int -> int
#Calcula los ingresos del cine, precioEntrada * espectadores
def ingresos(precioEntrada):
    return espectadores(precioEntrada)*precioEntrada

#gastos: ins -> int
#fijos + variables 
def gastos(precioEntrada):
    return 180000 - espectadores(precioEntrada)*40
ganancia = espectadores(precioEntrada)
print(ganancia)
