#José Carlos Mora 2ºDAM

print("Ejercicio 1")
#Evaluar un número

#Pide un número entero y muestra:

#“El número es positivo” si es mayor que 0.

#“El número es negativo” si es menor que 0.

#“El número es cero” en cualquier otro caso.


num = int(input("Introduce un numero: "))
if(num>0):
    print("El numero es positivo")
elif(num<0):
    print("El numero es negativo")
else:
    print("El numero es cero")


print("Ejercicio 2")
#Pide dos números enteros y muestra uno de estos tres mensajes:

#“El primero es mayor que el segundo.”

#“El segundo es mayor que el primero.”

#“Ambos son iguales.”

num2 = int(input("Introduce un numero: "))
num3 = int (input("Introduce otro numero: "))
if(num2>num3):
    print("El primero es mayor que el segundo")
elif(num3>num2):
    print("El segundo es mayor que el primero")
else:
    print("Ambos son iguales")

print("Ejercicio 3")
#Pide una frase y una palabra, y muestra:

#“La palabra está en la frase.” si aparece,

#o “La palabra no se encuentra.” si no aparece.


frase = str(input("Introduce una frase: "))
palabra = str(input("Introduce una palabra: "))


frase = frase.lower()
palabra = palabra.lower()


palabras = frase.split()


encontrada = False

for p in palabras:
    if (p == palabra):
        encontrada = True

if (encontrada):
    print("La palabra está en la frase")
else:
    print("La palabra no se encuentra")


print("Ejercicio 4")
#Pide un texto y muestra:

#“Empieza por mayúscula.” si el texto empieza por una letra mayúscula.

#“Termina en punto.” si finaliza con un punto (.).

#“El texto no cumple las condiciones.” si no cumple ninguna de las dos.

texto = str(input("Introduce una frase: "))

if(frase[0].isupper):
    print("Empieza por mayúscula")
elif(frase[-1].endswith(".")):
    print("Termina en punto")
else:
    print("El texto no cumple las condiciones")

print("Ejercicio 5")
#Pide una nota numérica (de 0 a 10) y muestra el nivel del alumno según la nota

nota = int(input("Introduce una nota: "))
if(nota>=0 and nota<=4):
    print("Insuficiente")
elif(nota==5):
    print("Suficiente")
elif(nota==6):
    print("Bien")
elif(nota>=7 and nota<=8):
    print("Notable")
elif(nota>=9 and nota <=10):
    print("Sobresaliente")
else:
    print("Nota no válida")

