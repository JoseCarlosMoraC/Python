#Jose Carlos Mora 2ºDAM

#Vas a crear un pequeño gestor de notas que registre las calificaciones de varios alumnos, calcule sus medias y determine si aprueban o suspenden.

print("Ejercicio 1")


numAlumnos = int(input("Introduce el número de alumnos: "))


while (numAlumnos <= 0):
    numAlumnos = int(input("El número debe ser mayor que 0. Introduce de nuevo: "))


sumaMedias = 0
aprobados = 0
mejorar = 0
suspensos = 0


i = 0
while (i < numAlumnos):
    print("Alumno", i + 1)
    nombre = str(input("Nombre: "))


    numNotas = int(input("¿Cuántas notas tiene " + nombre + "? "))
    while (numNotas <= 0):
        numNotas = int(input("Debe ser mayor que 0. Introduce de nuevo: "))


    suma = 0
    for j in range(numNotas):
        nota = float(input("Introduce la nota " + str(j + 1) + ": "))
        suma = suma + nota


    media = suma / numNotas
    sumaMedias = sumaMedias + media


    if (media >= 5):
        print("Media de", nombre, ":", round(media, 2), "-> Aprobado")
        aprobados = aprobados + 1
    elif (media >= 4):
        print("Media de", nombre, ":", round(media, 2), "-> Necesita mejorar")
        mejorar = mejorar + 1
    else:
        print("Media de", nombre, ":", round(media, 2), "-> Suspenso")
        suspensos = suspensos + 1

    i = i + 1


mediaGrupo = sumaMedias / numAlumnos

print("--- RESUMEN FINAL ---")
print("Media del grupo:", round(mediaGrupo, 2))
print("Aprobados:", aprobados)
print("Necesita mejorar:", mejorar)
print("Suspensos:", suspensos)
