#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 2
n = int(input("n es un numero entero positivo:  "))
b = int(input("b es un numero entero positivo menor que 10:  "))
if n <= 0 or b < 2 or b >= 10:
    print("Los valores ingresados no son válidos")
else:
    resultado = ""
    while n > 0:
        residuo = n % b
        resultado = str(residuo) + resultado
        n = n // b
    print(f"El número en base {b} es: {resultado}") 