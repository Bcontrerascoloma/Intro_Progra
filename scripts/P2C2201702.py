from types import _ReturnT_co
import estructura
#alumno: nombre(str) sexo(str)
estructura.crear(“alumno”,”nombre sexo”)
#arbol: valor(alumno) izq(arbol) der(arbol)
estructura.crear(“arbol”,”valor izq der”)
#ejemplo:
A=arbol(alumno(“jose”,”M”), arbol(alumno(“gabi”,”F”),alumno(“Ana”,None,None),None),arbol(alumno(“rosa”,”F”),None,None))


#invocaciones:: arbol(alumno) alumno -> int
#entregue el número de invocaciones a la función que se realizan para encontrar (o no) el nombre
def invocaciones(A, nombre):
    assert type(A) == arbol
    assert type(nombre) == str
    if A == None:
        return 0
    if A.valor.nombre == nombre
        return 1 
    else:
        return invocaciones(A.izq)+(
