#Escribir una función a la que se le pase una cadena <nombre> y muestre 
# por pantalla el saludo ¡hola <nombre>!.

nombre=str(input("Dime tu nombre"))

def saludar(nombre):
    print("hola",nombre)


saludar(nombre)
