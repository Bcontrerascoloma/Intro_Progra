
#LAS FUNCIONES PUEDEN ALMACENARSE COMO UNA VARIABLE 
def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicacion(x,y):
    return x*y
sumador = suma
assert suma(1,2) == sumador(1,2)
#PODEMOS ENTREGAR FUNCIONES COMO ARGUMENTO EN OTRA FUNCION 

def operarGeneral(a,b,fun):
    resultado = fun(a,b)
    return resultado
#print(operarGeneral(1,2,suma))


#LAMDA FUNCTIONS

#unafuncion = lamda x,y,z: x+y+z
#sin receta de diseño ni nombre ni testing
suma = lambda x,y : x+y
saludador = lambda nombre: print("Hola",nombre)
#saludador("bruno")
a = 10
b = 20
mensaje = "a es mayor que b" if a > b else "a es menor que b"
print(mensaje)
#como escribir funcion esPar en lamda
#esPar = lambda n: True if n%2==0 else False
esPar = lambda n: n%2==0
assert esPar(20) == True
