#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.

vacio = []
for i in range(6):
    vacio.append(int(input("Introduce un número ganador: ")))
vacio.sort()
print("Los números ganadores son " + str(vacio))