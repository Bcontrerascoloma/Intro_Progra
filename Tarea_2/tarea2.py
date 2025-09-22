import estructura
estructura.crear("pasajero", "rut nombre categoria")
#esPasajeroValido: pasajero -> bool
#devuelve True si es un pasajero valido y False si no lo es
#ejemplo: esPasajeroValido(pasajero(221424247,"Benjamin", "Gold"))
#ejemplo: esPasajeroValido(pasajero(123456789,"Antonia",23))
def esPasajeroValido(p):
    return type(p) == pasajero \
    and type(p.rut) == int and type(p.nombre) == str \
    and type(p.categoria) == str and \
    p.categoria == "Elite Plus" or p.categoria == "Diamond" or p.categoria == "Platinum" or p.categoria == "Gold" or p.categoria == "Flyer" or p.categoria == "No Fidelizado"
assert esPasajeroValido(pasajero(221424247,"Benjamin","Gold"))
assert not esPasajeroValido(pasajero(123456789,"Antonia",23))

