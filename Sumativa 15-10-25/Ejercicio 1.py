#Revisa el siguiente código y corrige los errores para que se pueda ejecutar correctamente la suma de dos números. 

#Añado un float a las variables para convertir el valor introducido a numérico y facilitar la suma. 
var1 = float(input("Introduce el primer número: "))
#He añadido las comillas en el input para que sea un valor string. Si no estuvieran, daría error. 
var2 = float(input("Introduce el segundo número: "))

#He convertido var total en var_total porque python no acepta variables con espacios en medio. 
var_total = var1 + var2

#La f del principio del print no va seguida de una coma, y las variables se encierran en llaves y no en paréntesis. 
print(f"El resultado de sumar {var1} y {var2} es", var_total)