i=1
lista=[]
while i !=0:
    print("1.")
    print("2.")
    print("3.")
    print("4.")

    preg=int(input("Di un numero"))

    if preg ==1:
        v=int(input("Que numero quieres añadir"))
        lista.append(v)
        print(lista)
    elif preg == 2:
        num = int(input("Que  numero quieres añadir?: "))
        pos = int(input("Introduce la posicion: "))
        pos = pos - 1
        lista.insert(pos,num)
        print(f"El numero {num} ha sido añadido")
    elif preg == 3:
        longitud=len(lista)
        print(longitud)
    elif preg == 4:
        lista.pop()
    elif preg == 5:
        n = int(input("¿Que numero desea eliminar?"))
        lista.remove(n)
    elif preg == 7:
        posicion = int(input("dime un numero"))
        contador = 0
        for numero in lista:
            contador=contador+1
            print(numero)
            if numero==posicion:
                print(contador)
    elif preg == 8:
        print(lista)
    elif preg == 9:
        print("Saliendo del programa")
        i=0
    else:
        print("Opcion",preg)