import tarea2 as t
from lista import *
# --- tests para listarCategoria ---
# Creamos algunos pasajeros
p1 = t.pasajero(123456789, "Juan", "Gold")
p2 = t.pasajero(987654321, "Ana", "Platinum")
p3 = t.pasajero(111222333, "Luis", "Gold")
p4 = t.pasajero(444555666, "Carla", "Flyer")

# Construimos la lista usando tus primitivas
L = lista(p1, lista(p2, lista(p3, lista(p4, listaVacia))))

# Probamos que sólo se obtengan los pasajeros Gold
resultado_gold = t.listarCategoria(L, "Gold")
print("Pasajeros Gold:", resultado_gold)

# Esperado: lista con p1 y p3
assert cabeza(resultado_gold) == p1
assert cabeza(cola(resultado_gold)) == p3

# Probamos con Platinum
resultado_platinum = t.listarCategoria(L, "Platinum")
print("Pasajeros Platinum:", resultado_platinum)

# Esperado: lista con p2
assert cabeza(resultado_platinum) == p2

# Probamos con categoría inexistente
resultado_inexistente = t.listarCategoria(L, "No Fidelizado")
print("Pasajeros No Fidelizado:", resultado_inexistente)

# Esperado: lista vacía
assert esListaVacia(resultado_inexistente)

print("Todos los tests pasaron correctamente")

