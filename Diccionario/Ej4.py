#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
#por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
#el nombre del mes.

f=str(input("Dime la fecha en formato dd/m/aaaa"))

meses={1:'enero',2:'febrero',3:'marzo',4:'abril'}
dia, mes, año = f.split("/")
print(f'Hoy es {dia} de  {meses[mes]}donde  de {año}')