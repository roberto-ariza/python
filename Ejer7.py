#Escribir un programa que pida al usuario su peso (en kg) y estatura
#  (en metros),calcule el índice de masa corporal y lo almacene 
# en una variable, y muestre por pantalla la frase Tu índice de masa
#  corporal es <imc> donde <imc> es el índice de masa corporal 
# calculado redondeado con dos decimales.

peso=float(input("Dime tu  peso: "))
estatura=float(input("Dime tu altura: "))
imc=peso/(estatura**2)
print("Tu imc es ",round(imc, 2))