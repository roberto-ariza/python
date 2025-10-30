#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

dato1=float(input("Cantidad  a invertir"))
interes=float(input("Interes anual"))
n=int(input("Numero de años"))

capitalFinal=dato1*(1+interes)**n
print(capitalFinal)