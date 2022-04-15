# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    suma = 0
    
    with open ('archivos_python\stock.csv') as csvfile:
        stock = list(csv.DictReader(csvfile))
    
    for row in stock:
        for item, cantidad in row.items():
            if item == 'tornillos':
                suma += int(cantidad)
   
    print ("El total de tornillos es =", suma)
    csvfile.close()       




def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    cant_2amb = 0
    cant_3amb = 0

    with open ('archivos_python\propiedades.csv') as csvfile:
        propiedades = list(csv.DictReader(csvfile))

    for row in propiedades:
        try:
            if row['ambientes'] == '2':
                cant_2amb += 1
            elif row['ambientes'] == '3':
                cant_3amb += 1
        except:
            print('No hay departamentos de 2 o 3 ambientes')
    
    print('La cantidad de deptos de 2 ambientes es:', cant_2amb, 'y de 3 ambientes:', cant_3amb)
    csvfile.close()    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
