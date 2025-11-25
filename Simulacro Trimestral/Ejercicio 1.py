inicio = int(input("Introduce el inicio del intervalo: "))
fin = int(input("Introduce el fin del intervalo: "))

incremento = int(input("Introduce el incremento para el intervalo: "))

salida = ""

for i in range(inicio + incremento, fin + 1, incremento):
    if not i % 4 == 0:
        if i % 6 == 0:
            salida = salida + (", " + "*" + f"{i}" + "*")
        else:
            salida = salida + (", " + f"{i}")

print(str(inicio) + salida)