#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 10
n = int(input("Ingrese un entero positivo n: "))
if n < 2:
    print("No hay números primos menores o iguales a n (los primos comienzan desde 2).")
else:
    contador_primos = 0
    mayor_primo = 0
    print(f"Números primos menores o iguales a {n}:")
    # Recorremos todos los números desde 2 hasta n
    i = 2
    while i <= n:
        es_primo = True
        # Buscamos divisores únicamente hasta la raíz cuadrada de i (d * d <= i).
        # Justificación: Si un número 'i' se puede factorizar como i = a * b, al menos uno de 
        # los factores (a o b) debe ser menor o igual a la raíz cuadrada de i. Si no encontramos 
        # ningún divisor en ese rango, significa que tampoco existirá en el rango superior, 
        # ahorrando muchas iteraciones innecesarias.
        d = 2
        while d * d <= i:
            if i % d == 0:
                es_primo = False
                break
            d = d + 1
        if es_primo:
            print(i, end=" ")
            contador_primos = contador_primos + 1
            mayor_primo = i
        i = i + 1
    print(f"\n\nTotal de primos encontrados: {contador_primos}")
    print(f"El mayor número primo es: {mayor_primo}")