traductor = {}

# Pedir los pares palabra:traducción
entrada = input("Introduce las palabras (español:inglés) separadas por comas:\n")

pares = entrada.split(",")

for par in pares:
    esp, ing = par.split(":")
    traductor[esp.strip()] = ing.strip()

print("Diccionario creado:", traductor)

# Traducir frases
while True:
    frase = input("\n¿Qué frase quieres traducir?: ")
    frase_split = frase.split()

    for i in range(len(frase_split)):
        palabra_actual = frase_split[i]
        if palabra_actual in traductor:
            frase_split[i] = traductor[palabra_actual]

    resultado = " ".join(frase_split)
    print("Traducción:", resultado)

    continuar = input("¿Quieres continuar? (si/no): ").lower()
    if continuar == "no":
        break
