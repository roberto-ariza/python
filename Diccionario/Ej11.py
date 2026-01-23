directorio="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

#dividir cadena por cada /n

linea=directorio.split('\n')
claves=linea[0].split(';')

directorio2={}

for i in range(1,len(linea)):
    datos=linea[i].split(';')
    print(datos)
