cifras = int(input("Introduce la cantidad de cifras: "))
numero = int(input("Introduce un número con esa cantidad de cifras: "))

producto = 1
pares = 0

if len(str(numero)) == cifras:
    for i in range(len(str(numero))):
        letra = int(str(numero)[i])
        producto = producto * letra
        if letra % 2 == 0:
            pares += 1

    print(f"Producto de las cifras: {producto}")
    print(f"Cifras pares: {pares}")
else:
    print("Longitud incorrecta. ")