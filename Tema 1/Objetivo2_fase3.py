#José Carlos Mora 2ºDAM



#Crea tres listas con nombres de productos: ordenadores, periféricos y accesorios.
ordenadores = ["Portátil", "Sobremesa", "Servidor"]
perifericos = ["Ratón", "Teclado", "Monitor"]
accesorios = ["Funda", "Altavoces", "Webcam"]




#Crea una tupla con tres precios base distintos.
precios = (750, 1200, 2200)



#Crea un diccionario llamado catalogo donde cada clave sea una categoría (“Ordenadores”, “Periféricos”, “Accesorios”) y su valor sea la lista correspondiente
catalogo = {
    "Ordenadores": ordenadores,
    "Periféricos": perifericos,
    "Accesorios": accesorios
}


#Muestra por pantalla:
#Las tres listas.
#La tupla de precios.
#El contenido completo del diccionario.
#Un acceso concreto: el segundo periférico.

print(ordenadores)
print(perifericos)
print(accesorios)
print(precios)
print(catalogo)
print("Segundo periférico:",perifericos[1])

#He creado tres listas con nombres de productos
#He definido una tupla con tres precios base distintos
#Después, he creado un diccionario llamado catalogo donde cada clave corresponde a una categoría y su valor es la lista de productos de esa categoría
#Al final he mostrado por pantalla las tres listas, la tupla de precios, el contenido completo del diccionario y un acceso concreto al segundo periférico