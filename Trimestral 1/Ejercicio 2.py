#Inicializamos las variables. 
positivos = 0
negativos = 0

#En el bucle repetimos el proceso de pedir un número, y lo sumamos a la variable que corresponda. 
for i in range(6):
    numero = int(input(f"Introduce el número {i + 1}: "))
    if numero >= 0:
        positivos += numero
    else:
        negativos += numero
        
#Por último, mostramos la suma de los valores positivos y negativos una vez acaba el bucle.         
print(f"Suma de números positivos: {positivos}")
print(f"Suma de números negativos: {negativos}")