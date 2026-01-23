diccio={}
while True:
    print("1.Anadir cliente")
    print("2.Eliminar cliente")
    print("3.Mostrar datos")
    print("4.Mostrar lista ")
    print("5.Mostar lista clientes preferentes")
    print("6.Terminar programa")
    opcion=int(input("Dime que opcion deseas : "))

    if opcion==1:
        nif = input("NIF: ")
        nombre = input("Nombre: ")
        direccion = input("Dirección: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        preferente = str(input("¿Es preferente? (si/no): "))

        if preferente=="si":
            preferente=True
        else:
            preferente=False


        diccio[nif]={'nombre':nombre,'direccion':direccion,'telefono':telefono,'correo':correo,'preferente':preferente}

        print("cliente anadido")

    elif opcion==2:
        nif=int(input("Dime tu nif"))

        if nif in diccio:
            del diccio[nif]
            print("cliente eliminado")
        else:
            print("Ese cliente no existe")
    
    
    elif opcion==3:
        nif=input("IF del cliente")
        

    elif opcion==4:
        for nif, datos in diccio.items():
            print(f"NIF", {nif} ,"Nombre :" ,{datos['nombre']})
    
    elif opcion==5:
        for nif, datos in diccio.items():
            if datos['preferente']:
                print(f"NIF",{nif},"Nombre",{nombre},"Preferencia",{preferente})

    elif opcion==6:
        break   