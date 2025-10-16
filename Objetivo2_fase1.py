#José Carlos Mora 2ºDAM

print("Ejercicio 1")
#Pide dos enteros y muestra suma, resta, multiplicación y división.
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

print("Suma:", num1 + num2)
print("Resta:", num1 - num2)
print("Multiplicación:", num1 * num2)
print("División:", num1 / num2)




print("Ejercicio 2")
#Pide tres reales (float), calcula el promedio y muéstralo redondeado a 2 decimales.
real1 = float(input("Introduce un número: "))
real2 = float(input("Introduce otro número: "))
real3 = float(input("Introduce otro número más: "))

promedio = round((real1 + real2 + real3) / 3, 2)
print("El promedio es:", promedio)


print("Ejercicio 3")
#Pide dos enteros y muestra:
#si el primero es mayor que el segundo,
#si son iguales,
#si el segundo es distinto de 0.
num3 = int(input("Introduce un número: "))
num4 = int(input("Introduce otro número: "))

print("¿El primero es mayor?", num3 > num4)
print("¿Son iguales?", num3 == num4)
print("¿El segundo es distinto de cero?", num4 != 0)



print("Ejercicio 4")
#Pide dos valores lógicos escritos como True o False y muestra:
#and,
#or,
#not del primero,
#not del segundo.

valor1 = eval(input("Introduce el primer valor lógico (True/False): "))
valor2 = eval(input("Introduce el segundo valor lógico (True/False): "))

print("Resultado de and:", valor1 and valor2)
print("Resultado de or:", valor1 or valor2)
print("Resultado de not primer valor:", not valor1)
print("Resultado de not segundo valor:", not valor2)



print("Ejercicio 5")
#Pide dos edades como texto, convierte a entero y muestra suma y promedio (1 decimal).
edad1 = int(input("Introduce una edad: "))
edad2 = int(input("Introduce otra: "))

suma = edad1 + edad2
promedio = round(suma / 2, 1)
print("Suma total:", suma)
print("Promedio:", promedio)




print("Ejercicio 6")
#Pide dos números (pueden ser reales) y muestra:
#(a > 10) and (b < 5)
#(a == b) or (b > 0)
#not (a < b)
num5 = float(input("Introduce un número: "))
num6 = float(input("Introduce otro número: "))

print("(a > 10) and (b < 5):", (num5 > 10) and (num5 < 5))
print("(a == b) or (b > 0):", (num5 == num6) or (num6 > 0))
print("not (a < b):", not (num5 < num6))



print("Ejercicio 7")
#Pide dos reales, divide y muestra el resultado redondeado a 1 decimal.
num7 = float(input("Introduce un número: "))
num8 = float(input("Introduce otro número: "))

print("Resultado redondeado:", (round(num7 / num8, 1)))
