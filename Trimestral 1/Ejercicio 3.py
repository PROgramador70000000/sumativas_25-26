#Le pedimos al usuario que introduzca las variables que necesitamos. 
cifras = int(input("Introduce un número de cifras: "))
numero = int(input("Introduce un número con las cifras indicadas anteriormente: "))

#Inicializamos las variables que necesitemos para más tarde. 
suma = 0
longitud = int(len(str(numero)))

#Controlando bien los formatos de las variables, comprobamos si las cifras son las del nñumero introducido. 
#Si es así, sumamos la cifra que corresponda al total. 
#Al final del bucle, mostramos la suma de las cifras del número introducido. 
if longitud == cifras:
    for i in range(longitud):
        letra = str(numero)[i]
        suma += int(letra)

    print(f"Resultado: {suma}")
else:
    print("Error, no coincide el número de cifras. ")