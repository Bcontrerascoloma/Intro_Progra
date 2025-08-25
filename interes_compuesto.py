# interesCompuesto: int num num -> int
# la funcion calcula el monto final a partir de capital,tasa,tiempo.
# ejemplo: interesCompuesto(1000,5,10) -> 1628
def interesCompuesto(capital,tasa,tiempo):
    return int(capital*(1+(tasa/100))**tiempo)
assert interesCompuesto(1000,5,10) == 1628
#Programa
capital = int(input("Capital inicial: "))
tasa = float(input("Tasa de interés anual(%): "))
tiempo = int((input("Años: ")))
monto_final = interesCompuesto(capital,tasa,tiempo)
formato = print(f"Monto final después de {tiempo} años: ${monto_final}")
