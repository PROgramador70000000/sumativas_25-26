#Primero, inicializamos las variables. 
var_min = int(input("Introduce el número más bajo: "))
var_max = int(input("Introduce el número más alto: "))
intervalo = int(input("Introduce el intervalo entre esos dos números: "))

salida = ""

#Ahora, omitimos el valor inicial en la salida para evitar esa coma final innecesaria. 
#Concatenamos los demás valores. 
for i in range(var_min + intervalo, var_max + 1, intervalo):
    salida = salida + (", " + str(i))

#Mostramos la salida más el valor inicial que hemos omitido antes. 
print(str(var_min) + salida)