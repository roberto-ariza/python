#Los tramos impositivos para la declaración de la renta en un determinado país son
#los siguientes:

renta=int(input("Cual es tu renta anual"))

if renta<10000:
    print("Tipo impositivo 5%")
elif renta>10000 and renta<20000:
    print("Tipo impositivo 15%")
elif renta>20000 and renta<35000:
    print("Tipo impositivo 20%")
elif renta>35000 and renta<60000:
    print("Tipo impositivo 30%")
elif renta>60000:
    print("Tipo impositivo 45%")
else:
    print("Error")