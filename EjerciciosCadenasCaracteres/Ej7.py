#Escribir un programa que pregunte el correo 
# electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico 
# con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

email=str(input("introduzca un correo electronico : "))
usuario=email[:email.find("@")]
new=usuario+"@ceu.es"
print(new)
