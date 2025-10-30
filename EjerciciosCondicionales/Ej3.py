#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

num1=int(input("introduzca numero 1 :"))
num2=int(input("introduzca numero 2 :"))


if num2==0:
    print("error")
else:
    total=num1/num2
    print(total)

    
