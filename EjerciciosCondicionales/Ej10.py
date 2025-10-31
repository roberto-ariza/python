#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
#Los ingredientes para cada tipo de pizza aparecen a continuación. 
#● Ingredientes vegetarianos: Pimiento y tofu. 
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
#en función de su respuesta le muestre un menú con los ingredientes disponibles 
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el 
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la 
#pizza elegida es vegetariana o no y todos los ingredientes que lleva. 

# Programa: Pizzería Bella Napoli

que = input("¿Quieres una pizza vegetariana o no vegetariana? (responde 'vegetariana' o 'no'): ")

if que == "vegetariana":
    print("Ingredientes disponibles: Pimiento y Tofu.")
    ingrediente = input("¿Cuál quieres? : ")
    print(f"\nHas elegido una pizza VEGETARIANA con mozzarella, tomate y {ingrediente}.")
elif que == "no":
    print("Ingredientes disponibles: Peperoni, Jamón y Salmón.")
    ingrediente = input("¿Cuál quieres? : ")
    print(f"\nHas elegido una pizza NO VEGETARIANA con mozzarella, tomate y {ingrediente}.")
else:
    print("Opción no válida. Debes escribir 'vegetariana' o 'no'.")

