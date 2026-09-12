#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 5
suma = 0
cantidad = 0
print("Ingrese números enteros (ingrese 0 para terminar):")
n = int(input("Número: "))
while n != 0:
    if n % 2 == 0:
        suma = suma + n
        cantidad = cantidad + 1
    n = int(input("Número: "))
if cantidad == 0:
    print("No se ingresó ningún número par.")
else:
    media = suma / cantidad
    print(f"La media de los valores pares es: {media}")