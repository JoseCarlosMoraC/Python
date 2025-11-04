def sumar():
    num = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado de la suma: {num + num2:.2f}")

def restar():
    num = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado de la resta: {num - num2:.2f}")

def multiplicar():
    num = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("Resultado de la multiplicación: {num * num2:.2f}")

def dividir():
    num = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Resultado de la división: {num / num2:.2f}")


def potencia():
    base = float(input("Base: "))
    exponente = float(input("Exponente: "))
    print("Resultado: {base ** exponente:.2f}")

def raiz_cuadrada():
    num = float(input("Número: "))
    if num < 0:
        print("Error: No se puede calcular la raíz de un número negativo.")
    else:
        print("Resultado: {num ** 0.5:.2f}")

def modulo():
    num = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    if num2 == 0:
        print("Error: No se puede calcular módulo con divisor cero.")
    else:
        print("Resultado: {num % num2:.2f}")


def operaciones_avanzadas():
    subopcion = ''
    while subopcion != 'd':
        print("Operaciones avanzadas:")
        print("a) Potencia")
        print("b) Raíz cuadrada")
        print("c) Módulo")
        print("d) Volver")
        subopcion = input("Selecciona una opción: ")

        if subopcion == 'a':
            potencia()
        elif subopcion == 'b':
            raiz_cuadrada()
        elif subopcion == 'c':
            modulo()
        elif subopcion == 'd':
            pass
        else:
            print("Opción no válida. Intenta de nuevo.")

def menu():
    opcion = ''
    while opcion != '6':
        print("=========================")
        print("  CALCULADORA AVANZADA")
        print("=========================")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Operaciones avanzadas")
        print("6) Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            sumar()
        elif opcion == '2':
            restar()
        elif opcion == '3':
            multiplicar()
        elif opcion == '4':
            dividir()
        elif opcion == '5':
            operaciones_avanzadas()
        elif opcion == '6':
            print("Fin del programa. ¡Hasta pronto!")
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()
