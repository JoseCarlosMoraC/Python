class Autor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def mostrar_autor(self):
        print("Autor: {self.nombre} {self.apellidos}")


class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = None

    def anadir_autor(self, autor):
        self.autor = autor

    def mostrar_libro(self):
        print("Título: {self.titulo}")
        print("ISBN: {self.isbn}")
        if self.autor:
            self.autor.mostrar_autor()
        else:
            print("Autor: No asignado")


class Biblioteca:
    def __init__(self):
        self.lista_libros = []
    def numero_libros(self):
        print("El número de libros en la biblioteca es: {len(self.lista_libros)}")
    def anadir_libro(self, libro):
        self.lista_libros.append(libro)
    def borrar_libro(self, titulo):
        encontrados = []
        for libro in self.lista_libros:
            if libro.titulo.lower() != titulo.lower():
                encontrados.append(libro)
        if len(encontrados) != len(self.lista_libros):
            print(f"El libro '{titulo}' ha sido eliminado.")
        else:
            print(f"No se encontró el libro con título '{titulo}'.")
        self.lista_libros = encontrados
    def mostrar_biblioteca(self):
        if len(self.lista_libros) == 0:
            print("La biblioteca está vacía.")
        else:
            for libro in self.lista_libros:
                libro.mostrar_libro()
                print("--------------------")



def mostrar_menu():
    print("Menu")
    print("1) Añadir libro a la biblioteca")
    print("2) Mostrar biblioteca")
    print("3) Borrar libro")
    print("4) ¿Número de libros?")
    print("5) Salir")


def anadir_libro_a_biblioteca(biblioteca):
    titulo = input("Introduzca el título del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    nombre_autor = input("Introduzca el nombre del autor: ")
    apellidos_autor = input("Introduzca el apellido del autor: ")


    autor = Autor(nombre_autor, apellidos_autor)
    libro = Libro(titulo, isbn)
    libro.anadir_autor(autor)
    biblioteca.anadir_libro(libro)



def borrar_libro_de_biblioteca(biblioteca):
    titulo = input("Introduzca el título del libro a eliminar: ")
    biblioteca.borrar_libro(titulo)



if __name__ == "__main__":
    biblioteca = Biblioteca()
    opcion = 0

    while opcion != 5:
        mostrar_menu()
        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            anadir_libro_a_biblioteca(biblioteca)
        elif opcion == 2:
            biblioteca.mostrar_biblioteca()
        elif opcion == 3:
            borrar_libro_de_biblioteca(biblioteca)
        elif opcion == 4:
            biblioteca.numero_libros()
        elif opcion == 5:
            print("¡Adiós!")
        else:
            print("Opción no válida.")
