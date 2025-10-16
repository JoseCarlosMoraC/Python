# José Carlos Mora 2ºDAM

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

variable1 = (a < b) and (b < c)
variable2 = (a == b) or (b == c)
variable3 = not (a > c)
print("(a < b) and (b < c):",variable1)  
print("(a == b) or (b == c):",variable2) 
print("not (a > c):",variable3)    


#He solicitado al usuario por pantalla tres números enteros 
#Comprueba si el primero es menor que el segundo y el segundo menor que el tercero
#Comprueba si el primero es igual al segundo o el segundo igual al tercero
#Comprueba si el primero es mayor que el tercero
#Después, he mostrado por pantalla el resultado 
