#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 4
numero_base = int(input(" Que numero quiere intercalar? "))
if numero_base <= 0:
    print("El numero debe ser mayor a 0")
else:
    numero_intercaldo = 0
    texto_base = str(numero_base)
    texto_intercalado = str(numero_intercaldo)
    numero_final = texto_intercalado.join(texto_base)
    print(f"El numero intercalado es: {numero_final}")