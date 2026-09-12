#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 1
Opcion = input("Ingrese una opción (1-4): ")
if Opcion == "1":
    grados = float(input("Introduzca el ángulo en grados: "))
    terminos = int(input("Introduzca el número de términos: "))
    pi = 3.141592653589793
    x = grados * (pi / 180.0)
    if terminos <= 0:
        print("La cantidad de términos debe ser mayor a 0.")
    elif terminos == 1:
        seno = x
        print(f"El resultado aproximado es: {seno}")
    else:
        seno = 0.0
        for n in range(terminos):
            signo = 1 if n % 2 == 0 else -1
            exponente = 2 * n + 1
            potencia = 1.0
            for _ in range(exponente):
                potencia *= x
            factorial = 1
            for i in range(1, exponente + 1):
                factorial *= i
            seno += signo * (potencia / factorial)
            
        print(f"El resultado aproximado es: {seno}")
if Opcion == "2":
    grados = float(input("Introduzca el ángulo en grados: "))
    terminos = int(input("Introduzca el número de términos: "))
    pi = 3.141592653589793
    x = grados * (pi / 180.0)
    if terminos <= 0:
        print("La cantidad de términos debe ser mayor a 0.")
    elif terminos == 1:
        coseno = 1.0
        print(f"El resultado aproximado es: {coseno}")
    else:
        coseno = 0.0
        for n in range(terminos):
            signo = 1 if n % 2 == 0 else -1
            exponente = 2 * n
            potencia = 1.0
            for _ in range(exponente):
                potencia *= x
            factorial = 1
            for i in range(1, exponente + 1):
                factorial *= i
            coseno += signo * (potencia / factorial)
            
        print(f"El resultado aproximado es: {coseno}")
if Opcion == "3":
    print("Opción 3 Tangente: Función en construcción.")
if Opcion == "4":
    print("Opción 4: Salir del programa.")
