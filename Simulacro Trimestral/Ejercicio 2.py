positivos = 0
negativos = 0
mayor_100 = 0

for i in range(7):
    numero = int(input(f"Introduce el número {i + 1}: "))
    if numero < 0:
        negativos += numero
    else:
        positivos += numero
    if numero > 100:
        mayor_100 += 1

print(f"Suma positivos: {positivos}")
print(f"Suma negativos: {negativos}")
print(f"Mayores de 100: {mayor_100}") 
        