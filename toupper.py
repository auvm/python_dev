#!/usr/bin/env python3
import sys

#sys.argv[] es el vector de argumentos, el indice [0] es el nombre del 
#script, el indice [1] y sucesivos son los argumentos
print("Nombre del archivo: ", sys.argv[1])

#with asegura que el archivo es propiamente cerrado aún si se presenta 
#una excepción

with open(sys.argv[1], 'r') as file:
	#se lee el contenido y pasa a la variable file_content
	file_content = file.read()

#ya hago la funcionalidad con el contenido del archivo
print(file_content.upper())
