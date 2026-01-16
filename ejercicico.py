diccionario={}
p=1
while p != 0:
    print("1.Añadir un dato")
    print("0.Salir")
    p=int(input("Elige una opcion"))
    if p == 1:
        dato=input("Añade un dato:")
        valor=input("Añade un valor al dato: ")
        diccionario[dato]=valor
        