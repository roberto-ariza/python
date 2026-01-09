#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.
dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
v=str(input("Que divisa desea buscar? : "))
if  v in dic:
    print(dic[v])
else:
    print("No se encuentra la divisa")

