#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 9
import math
epsilon = float(input("Ingrese la tolerancia epsilon (ej. 0.0001 para 10^-4): "))
suma = 0
n = 0
while True:
    # Término actual de la serie para pi/4
    termino = ((-1) ** n) / (2 * n + 1)
    # Detener la suma cuando el valor absoluto del último término sea menor que epsilon
    if abs(termino) < epsilon:
        break
    suma = suma + termino
    n = n + 1
aproximacion_pi = suma * 4
numero_terminos = n
error = abs(aproximacion_pi - math.pi)
print(f"Aproximación obtenida de pi: {aproximacion_pi}")
print(f"Número de términos utilizados: {numero_terminos}")
print(f"Error respecto a math.pi: {error}")