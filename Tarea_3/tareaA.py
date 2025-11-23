import estructura

# Definir la estructura 'animal'
estructura.mutable("animal", "identificador especie listaAvistamientos")

# variable de estado
lista_animales = []


# cargarAnimales : str,list -> list
# Propósito:
#   Lee un archivo con líneas "ID,especie" y agrega animales
#   a la lista dada, retornando la lista actualizada.
# Ej: cargarAnimales("animales.txt", [])
def cargarAnimales(nombreArchivo, lista_animales):
    archivo = open(nombreArchivo, "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")
            ident = partes[0]
            especie = partes[1]
            nuevo = animal(ident, especie, [])
            lista_animales.append(nuevo)

    archivo.close()
    return lista_animales


# agregarAvistamientos : str × list -> list
# Propósito: Lee un archivo con líneas tipo: PuestoX,ID,AAAA-MM-DD,HH:MM y agrega ese avistamiento al animal cuyo ID coincide.
# Ej: agregarAvistamientos("avistamientos.txt", lista_animales)
def agregarAvistamientos(nombreArchivo, lista_animales):
    archivo = open(nombreArchivo, "r", encoding="utf-8")
    for linea in archivo:
        linea = linea.strip()
        if linea != "":
            partes = linea.split(",")
            puesto = partes[0]
            ident  = partes[1]
            fecha  = partes[2]
            hora   = partes[3]
            avist = puesto + " " + fecha + " " + hora
            for a in lista_animales:
                if a.identificador == ident:
                    a.listaAvistamientos.append(avist)
                    break

    archivo.close()
    return lista_animales



# ----------------------------------------------------------
# zonaMasProbable : str × int × list -> str
# Propósito:
#   Dada una especie y una hora (entero HH),
#   retorna el puesto donde es más probable observarla.
# Ejemplo:
#   zonaMasProbable("ciervo", 17, lista_animales) → "Puesto7"
# ----------------------------------------------------------
def zonaMasProbable(especieAnimal, hora, lista_animales):
    puestos = []

    for a in lista_animales:
        if a.especie == especieAnimal:
            for av in a.listaAvistamientos:
                partes = av.split(" ")
                puesto = partes[0]
                horaAV = int(partes[2].split(":")[0])
                if horaAV == hora:
                    puestos.append(puesto)

    if len(puestos) == 0:
        return "No hay datos suficientes"

    mas_comun = puestos[0]
    max_rep = puestos.count(mas_comun)

    for p in puestos:
        rep = puestos.count(p)
        if rep > max_rep:
            max_rep = rep
            mas_comun = p

    return mas_comun



# ----------------------------------------------------------
# corregirHora : list -> None
# Propósito:
#   Corregir todos los avistamientos posteriores al
#   19 de octubre de 2025 restando una hora.
#   Caso borde: si la hora es 00:MM pasa a 23:MM del día anterior.
# Ejemplo:
#   "2025-10-20 00:30" -> "2025-10-19 23:30"
# ----------------------------------------------------------
def corregirHora(lista_animales):

    for a in lista_animales:
        for i in range(len(a.listaAvistamientos)):

            av = a.listaAvistamientos[i]
            partes = av.split(" ")

            puesto = partes[0]
            fecha  = partes[1]
            hora   = partes[2]

            if fecha > "2025-10-19":

                hhmm = hora.split(":")
                h = int(hhmm[0])
                m = hhmm[1]

                h = h - 1

                # CASO BORDE: hora pasa de 00 → 23 y resta 1 día
                if h < 0:
                    h = 23

                    partesFecha = fecha.split("-")
                    anio = int(partesFecha[0])
                    mes  = int(partesFecha[1])
                    dia  = int(partesFecha[2]) - 1

                    diasMes = [31,28,31,30,31,30,31,31,30,31,30,31]

                    if dia == 0:
                        mes = mes - 1
                        dia = diasMes[mes - 1]
                        if mes == 0:
                            mes = 12
                            anio = anio - 1

                    if mes < 10:
                        mesStr = "0" + str(mes)
                    else:
                        mesStr = str(mes)

                    if dia < 10:
                        diaStr = "0" + str(dia)
                    else:
                        diaStr = str(dia)

                    fecha = str(anio) + "-" + mesStr + "-" + diaStr

                # Formateo de hora sin zfill
                if h < 10:
                    hStr = "0" + str(h)
                else:
                    hStr = str(h)

                nuevaHora = hStr + ":" + m

                a.listaAvistamientos[i] = puesto + " " + fecha + " " + nuevaHora

