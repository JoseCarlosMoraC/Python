# José Carlos Mora 2ºDAM

frase = input("Introduce una frase: ")

print("Ejercicio 1")
# La frase en distintos formatos (capitalize, upper, lower, swapcase)
print("--- FORMATO DEL TEXTO ---")
print("Capitalizada: ", frase.capitalize())
print("Mayúsculas: ", frase.upper())
print("Minúsculas: ", frase.lower())
print("Invertida: ", frase.swapcase())

print("\nEjercicio 2")
# Información sobre el contenido (isalpha, isdigit, isalnum, islower, isupper)
print("--- ANÁLISIS DEL CONTENIDO ---")
print("¿Solo letras?: ", frase.isalpha())
print("¿Solo números?: ", frase.isdigit())
print("¿Letras y números?: ", frase.isalnum())
print("¿Está en minúsculas?: ", frase.islower())
print("¿Está en mayúsculas?: ", frase.isupper())

print("\nEjercicio 3")
# El número total de caracteres y los caracteres reales (sin espacios)
print("--- LONGITUD ---")
print("Número total de caracteres: ", len(frase)) 
print("Caracteres reales (sin espacios):", len(frase.replace(" ", "")))

print("\nEjercicio 4")
# La frase sin espacios sobrantes (strip, lstrip, rstrip)
print("--- LIMPIEZA ---")
print("Sin espacios al principio: ", frase.lstrip()) 
print("Sin espacios al final: ", frase.rstrip())
print("Sin espacios en ambos lados: ", frase.strip())

print("\nEjercicio 5")
# La frase con una palabra reemplazada (replace)
buscar = input("Palabra a buscar: ")
nueva = input("Palabra nueva: ")
frase_modificada = frase.replace(buscar, nueva)
print("Frase modificada:", frase_modificada)

print("\nEjercicio 6")
# El carácter alfabéticamente mayor y menor (max, min)
print("--- CARACTERES ---")
print("Carácter mayor: ", max(frase)) 
print("Carácter menor: ", min(frase))  

print("\nEjercicio 7")
# La lista de palabras (split()) y su número
print("--- LISTA DE PALABRAS ---")
palabras = frase.split()
print("Lista: ", palabras)
print("Número de palabras: ", len(palabras))

print("\nEjercicio 8")
# La separación del texto usando / como separador (split("/"))
print("--- DIVISIÓN POR '/' ---")
print("Resultado del split ('/'): ", frase.split("/"))

print("\n--- ANÁLISIS COMPLETO FINALIZADO ---")
