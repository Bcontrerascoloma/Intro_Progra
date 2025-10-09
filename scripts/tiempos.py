import estructura

#Tiempo:: horas(int) minutos(int)
estructura.crear("Tiempo", "horas minutos")
Ti1 = Tiempo(2,30)
Ti2 = Tiempo(0,59)
Ti3 = Tiempo(3,5)
Ti4 = Tiempo(4,58)

def esTiempo(t):
    return ((type(t.horas) == int) and (0 <= t.horas) and (type(t.minutos) == int) and (0 <= t.minutos <=59)) 
assert esTiempo(Ti1)


def tiempoAstr(t):
    if t.horas >= 10:
        if t.minutos >=10:
            return (f"{t.horas}:{t.minutos}")
        else:
            return (f"{t.horas}:0{t.minutos}")
    else:
        if t.minutos >=10:
            return (f"0{t.horas}:{t.minutos}")
        else:
            return (f"0{t.horas}:0{t.minutos}")
assert tiempoAstr(Ti3) == "03:05"

def aMinutos(t):
    minutos = t.horas * 60 + t.minutos
    return minutos
assert aMinutos(Ti3) == 185

def crearTiempo(n):
    tiempo = Tiempo(n//60,n%60)
    return tiempo
assert crearTiempo(185) == Tiempo(3,5)

def sumarTiempos(T1,T2):
    tiempo = Tiempo(T1.horas+T2.horas+((T1.minutos+T2.minutos)//60),(T1.minutos+T2.minutos)%60)
    return tiempo
assert sumarTiempos(Ti3,Ti4) == Tiempo(8,3) 

def restarTiempo(T1,T2):
    T1 = aMinutos(T1)
    T2 = aMinutos(T2)
    Tf = T1 - T2
    if Tf > 0:
        return crearTiempo(Tf)
    else: 
        return Tiempo(0,0)
assert restarTiempo(Ti3,Ti4) == Tiempo(0,0)

def mayorTiempo(T1,T2):
    T1 = aMinutos(T1)
    T2 = aMinutos(T2)
    if T1 > T2:
        return crearTiempo(T1)
    else:
        return crearTiempo(T2)
assert mayorTiempo(Ti1,Ti2) == Tiempo(2,30)
        