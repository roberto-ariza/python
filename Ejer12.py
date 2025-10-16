#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

pan=float(input("numero de barras  de pan "))
barra=3.49
barraB=round(3.49*0.4,2)
total=round(pan*barra,2)
totalB=round(pan*barraB,2)
print("Has comprado ",pan,"el precio normal es ",total,"y el barato ",totalB)
