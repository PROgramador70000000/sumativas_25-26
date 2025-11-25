valor = 100
numero = 0

while numero >= 0 and valor >= 50 and valor <= 150:
    numero = int(input("Introduce un número: "))
    if numero % 2 == 0:
        valor /= 2
    elif numero % 2 != 0:
        valor += numero
    if numero % 3 == 0:
        valor -= 5

    print(f"\"Valor\" es {valor}")

print(f"Fin del programa. Valor es {valor}")