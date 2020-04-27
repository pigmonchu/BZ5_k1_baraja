palos = ('o', 'c', 'e', 'b')
cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')

baraja = []

for palo in palos:
    for carta in cartas:
       naipe = carta + palo
       baraja.append(naipe)

print(baraja)