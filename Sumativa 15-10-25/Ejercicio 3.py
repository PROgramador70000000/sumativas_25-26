#3. Crea un programa que calcule el área de un triángulo equilátero a partir de introducir por teclado el valor de un lado (a). Redondea el resultado a dos decimales. 

#Empezamos importando la librería math, que nos servirá para realizar esa raíz de más adelante. 
import math

#Determinamos el valor del lado...
lado = float(input("Introduce la longitud de un lado de un triángulo equilátero en cm: "))

#Y la operación la hacemos paso a paso; primero la raíz de 3, luego la fracción y luego multiplicamos eso por el cuadrado de a. 
raiz = math.sqrt(3)
fracción = raiz / 4
area = fracción * (lado ** 2)

#Por último, mostramos el valor del área del triángulo, no sin olvidar que las unidades cambian a cm cuadrados. 
print("El área del triángulo es de", round(area,2), "centímetros cuadrados. ")