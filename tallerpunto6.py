#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 6
suma = 0
suma_cuadrados = 0
cantidad = 0
print("Ingrese números enteros (ingrese 0 para terminar):")
n = int(input("Número: "))
while n != 0:
    suma = suma + n
    suma_cuadrados = suma_cuadrados + (n ** 2)
    cantidad = cantidad + 1
    n = int(input("Número: "))
if cantidad == 0:
    print("No se ingresó ningún número, se necesita al menos 1 valor para la poblacional.")    
if cantidad <= 1:
    print("Se necesitan al menos 2 valores para calcular la desviación estándar.")
else:
    varianza_poblacional = (suma_cuadrados - (suma ** 2 / cantidad)) / (cantidad)
    desviacion_poblacional = varianza_poblacional ** 0.5
    varianza_muestral = (suma_cuadrados - (suma ** 2 / cantidad)) / (cantidad - 1)
    desviacion_muestral = varianza_muestral ** 0.5
    print(f"La desviación estándar poblacional es: {desviacion_poblacional}")
    print(f"La desviación estándar muestral es: {desviacion_muestral}")