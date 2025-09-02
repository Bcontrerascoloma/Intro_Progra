
#contar_digito:: int int -> int
#recibe un numero n y un digito d retorna cuantas veces aparece d en n 
#ejemplo: contar_digito(112432123, 1) entrega 3
def contar_digito(n,d):
    if n <10:
        if n == d:
            return 1
        else:
            return 0
    if n%10 == d:
        return 1 + contar_digito(n//10,d)
    else:
        return (contar_digito(n//10,d))
#test
assert contar_digito(112432123, 1) == 3
assert contar_digito(12345678,9) == 0

def crear_string(n,d):
    c = contar_digito(n,d)
    if c == 0:
        return ""
    else:
        strc = str(c)
        strd = str(d)
        texto = (strc+strd+"-")
        return texto
assert crear_string(1221314,9) == ""
assert crear_string(1010102,2) == "12-"

def resumen_digitos(n,d=1):
#tenemos que convocar crear(n,1), guardarlo en algun lado, luego crear(n,1+1)
#el return deberia ser algo ai como return (crear)+ resuemn 
    if d > 9:
        return ""
    else:
        a = crear_string(n,d)
        recursed = a+ resumen_digitos(n,d+1)
        return recursed
assert resumen_digitos(1212) == "21-22-"
assert resumen_digitos(123456789) == "11-12-13-14-15-16-17-18-19-"
