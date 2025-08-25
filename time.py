#time int -> none
# Esta funcion cambia el tiempo de segundos a el resto de unidades
# ejemplo time(3665): NONE
second = int(input("Ingrese la cantidad de segundos: "))
def time(seconds):
    
    minutes = (seconds //60)
    
    second_rest = seconds%60
    hour = minutes//60
    print(f"""
    Cantidad de horas: {hour}
    Cantidad de minutos: {minutes}
    Cantidad de segundos: {second_rest} """)
time(second)
