#Escribir un programa que guarde en un diccionario los precios de las frutas de la
#tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
#precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
#mostrar un mensaje informando de ello.

diccionario={'platano':1.35,'manzana':0.80,'pera':0.85,'naranja':0.70}

f=input("Que fruta desea?: ")
k=float(input("Cuanto kg desea?: "))

if f in diccionario:
    resultado=diccionario[f]*k
    print(f"El precio de {f} es de ",resultado, "€ en total")
else:
    print(f"Esa fruta no existe o no la tenemos")