#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

leer=float(input("introduzca la puntuacion : "))
cantidad=2400 * leer

if leer == 0.0:
    nivel = "Inaceptable"
elif leer == 0.4:
    nivel="aceptable"
elif leer >= 0.6:
    nivel = "Meritorio"
else:
    nivel = None

if nivel:
    print("Tu nivel de rendimiento es",nivel)
    print("Recibirá" ,cantidad)
else:
    print("Puntuacion no valida debe ser 0.0, 0.4 o 0.6 mas")




