#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distinta.
compra=str(input("introduzac los productos de compras"))
new=compra.split(",")

for producto in new:
    print(producto)
