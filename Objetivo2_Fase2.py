#José Carlos Mora 2ºDAM


print("Ejercicio 1")
#Pide al usuario los siguientes datos con input():
#Nombre y apellidos
#Curso
#Grupo
#Carpeta del proyecto (solo el nombre, por ejemplo: Python)

nom = str(input("Introduce tu nombre completo: "))
curso = input("Introduce tu curso: ")
grupo = input("Introduce tu grupo: ")
carpeta = input("Introduce una carpeta(nombre): ")



print(
    "------------------------------\n"
    "Ficha del alumno/a\n"
    "------------------------------\n"
    "Nombre: \"" + nom + "\"\n"
    "Curso: " + curso + "\tGrupo: " + grupo + "\n"
    "Ruta del proyecto: C:\\Users\\" + nom + "\\" + curso + "\\" + carpeta + "\n"
    "------------------------------"
)
