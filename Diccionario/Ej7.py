diccionario={}
respuesta=0
total=0
while respuesta != "si":
    articulo = input("Que articulo quieres añadir: ")
    precio=float(input("¿Cual es el precio quieres añadir ?: "))
    diccionario[articulo]=precio
    total=total+precio
    respuesta=input("¿Quieres terminar la cesta?")
print("LISTA DE COMPRA")
for articulo, precio in diccionario.items():
    print(articulo, " = ",  precio ,"€")
print("Total de la cesta =",total ,"€")