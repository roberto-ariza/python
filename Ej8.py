#Escribir un programa que pregunte por consola el
#  precio de un producto en euros
#con dos decimales y muestre por pantalla el 
# número de euros y el número de
#céntimos del precio introducido.
precio=str(input("Indique precio de un producto : "))
new=precio.split(".")
euros=new[0]
cents=new[1]
print("El producto  vale",euros,"en €")
print("El producto vale",cents,"em cnts") 