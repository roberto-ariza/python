#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

horas=float(input("cuantas horas trabajadas?: "))
precio=float(input("cuanto cobras por hora?: "))
resultado= horas*precio
print(resultado,"€")