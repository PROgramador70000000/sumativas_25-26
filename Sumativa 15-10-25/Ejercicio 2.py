#2. Aprovechando el código del ejercicio anterior, crea un nuevo programa (en un nuevo fichero) y divide el resultado del ejercicio anterior entre 3. El resultado lo debes redondear con tres decimales. 

#Asignamos las variables. 
var1 = float(input("Introduce el primer número: "))
var2 = float(input("Introduce el segundo número: "))

#Realizamos la suma y la división del resultado de esta. 
var_suma = var1 + var2
var_divi = var_suma / 3

#Redondeamos el valor de la división a 3 decimales. 
var_divi = round(var_divi,3)

#Y mostramos los resultados. Utilizar los métodos string en este caso no es necesario, pero sí cómodo. 
print(f"El resultado de sumar {var1} y {var2} es", var_suma)
print(f"El resultado de dividir {var_suma} entre 3 es", var_divi)