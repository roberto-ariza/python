#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.

cantidad=int(input("Cantidad a  invertir : "))
interes=int(input("Interes anual : "))
year=int(input("num de años : "))
for i in range(1,year+1):
    cantidad=cantidad*(1+interes/100)
    print(cantidad)
