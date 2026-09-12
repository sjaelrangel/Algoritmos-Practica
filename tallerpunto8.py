#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 8
print("Clasificador de triángulos (ingrese 0 en la primera longitud para terminar):")
while True:
    a = float(input("Ingrese la longitud del primer lado: "))
    if a == 0:
        print("Programa finalizado.")
        break
    b = float(input("Ingrese la longitud del segundo lado: "))
    c = float(input("Ingrese la longitud del tercer lado: "))
    # Rechazar longitudes negativas o nulas
    if a <= 0 or b <= 0 or c <= 0:
        print("Error: Las longitudes deben ser mayores a cero. Intente nuevamente.\n")
        continue
    # Aplicar la desigualdad triangular
    # La suma de cualquier par de lados debe ser estrictamente mayor que el tercer lado
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Ordenamos los lados para identificar fácilmente cuál es el mayor (hipotética hipotenusa o lado c_max)
        lados = [a, b, c]
        lados.sort()
        menor, medio, mayor = lados[0], lados[1], lados[2]
        # Clasificación por sus lados
        if a == b and b == c:
            tipo_lados = "equilátero"
        elif a == b or b == c or a == c:
            tipo_lados = "isósceles"
        else:
            tipo_lados = "escaleno"
        # Clasificación por sus ángulos comparando cuadrados
        # Teorema de Pitágoras generalizado: a^2 + b^2 vs c^2 (donde 'mayor' es c)
        suma_cuadrados_menores = (menor ** 2) + (medio ** 2)
        cuadrado_mayor = mayor ** 2
        if suma_cuadrados_menores == cuadrado_mayor:
            tipo_angulos = "rectángulo"
        elif suma_cuadrados_menores > cuadrado_mayor:
            tipo_angulos = "acutángulo"
        else:
            tipo_angulos = "obtusángulo"
        print(f"-> Sí es un triángulo válido.")
        print(f"   Clasificación por lados: {tipo_lados}")
        print(f"   Clasificación por ángulos: {tipo_angulos}\n")
    else:
        print("-> Las longitudes ingresadas NO pueden formar un triángulo (no cumplen la desigualdad triangular).\n")