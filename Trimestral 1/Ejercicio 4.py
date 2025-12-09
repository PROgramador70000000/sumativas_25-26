#Inicializamos las variables. 
var_total = 50
valor = 1

#Mientras las condiciones no se cumplan, el bucle se repetirá para siempre. 
#Dentro del bucle, comprobamos si el número introducido es par y lo sumamos o restamos al valor. 
while valor != 0 or var_total <= 60:
    valor = int(input("Introduce un número, por favor: "))
    if valor % 2 == 0:
        var_total += valor
    else:
        var_total -= valor

    print(f"El valor total es de {var_total}")

#Una vez que alguna de las condiciones se cumple, acabamos el programa. 
print(f"El valor total es de {var_total}, y el programa ya ha acabado. ")
