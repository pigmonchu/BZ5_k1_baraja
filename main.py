import cartas

b = cartas.crea_baraja()
manos = cartas.repartir(b, 3, 5)

print(manos)