from Punto import Punto

messi=Punto()
elbicho=Punto()

a=messi.calcular_distancia(elbicho)

messi.x=8
messi.y=2

elbicho.x=9
elbicho.y=9

a=messi.calcular_distancia(elbicho)

print(a)