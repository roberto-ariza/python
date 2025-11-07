#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta


contraseña="contraseña"

pregunta=input("Dime contraseña : ")
i=0

while True:
    if(pregunta ==contraseña):
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        break
