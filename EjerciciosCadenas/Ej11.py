#Escribir un programa que pregunte el nombre el 
# un producto, su precio y un número
#de unidades y muestre por pantalla una cadena 
# con el nombre del producto seguido
#de su precio unitario con 6 dígitos enteros y 2
#  decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos 
# enteros y 2 decimales.

nombre=input("Dime el nombre del producto")
precio=float(input("Dime el precio del producto"))
numero=int(input("Dime el numero de unidades"))

total=precio*numero

preciostr=str(round(precio,2))

print("nombre ")



