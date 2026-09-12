#Taller 1 Algoritmos
#Sara Jael Rangel Pabon 2250799
#Rosa Valentina Plata Guevara 2250801
#Ejercicio 7
valores = []
print("Ingrese números enteros (ingrese 0 para terminar):")
n = int(input("Número: "))
while n != 0:
    valores.append(n)
    n = int(input("Número: "))
if len(valores) == 0:
    print("No se ingresaron valores.")
else:
    frecuencias = {}
    i = 0
    while i < len(valores):
        num = valores[i]
        if num in frecuencias:
            frecuencias[num] = frecuencias[num] + 1
        else:
            frecuencias[num] = 1
        i = i + 1
    max_frecuencia = 0
    for freq in frecuencias.values():
        if freq > max_frecuencia:
            max_frecuencia = freq
    if max_frecuencia == 1:
        print("Ningún valor se repite: todos los elementos tienen una frecuencia de 1, por lo que no existe una moda.")
    else:
        modas = []
        for num, freq in frecuencias.items():
            if freq == max_frecuencia:
                modas.append(num)
        if len(modas) > 1:
            print(f"El conjunto es multimodal. Hay varios valores con la misma frecuencia máxima ({max_frecuencia}): {modas}")
        else:
            print(f"La moda es: {modas[0]} (con una frecuencia de {max_frecuencia})")