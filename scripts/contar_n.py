"""
ESTRATEGIA:
(X) LEER UN NUMERO
(X) LEER VARIOS NUMEROS
(3) LEER VARIOS NUMEROS HASTA QUE LLEGUE NEGATIVO
(4) CONTAR CUANTOS NUMEROS LLEGARON
(5) CONTAR CUANTOS NUMEROS PARES LLEGARON
"""
def procedimiento(total=0): #argumento por omision 
    valor = int(input("Valor?"))
    if valor < 0:
        print("En total lei: " + str(total) + " valores pares")
        return
    if valor % 2==0:
        return procedimiento(total+1)
    else: 
        return procedimiento(total)
procedimiento()
