#Primero indicamos al usuario las condiciones de la contraseña. 
#Le ponemos un poco en contexto
print("JUEGO PASSWORD VERSIÓN 2")
print("En este pequeño juego aprenderás a crear una contraseña segura contra posibles piratas digitales. ")
print("-------------------------------------------------------------------------------------------------")
print("CONDICIONES: ")
print("1. La contraseña debe tener entre 6 y 8 caracteres. ")
print("2. La contraseña debe tener al menos dos números mayores o iguales a 1 y menores o iguales a 5. ")
print("3. La contraseña debe tener al menos dos letras minúsculas. ")
print("4. La contraseña debe tener al menos una letra mayúscula. ")
print("5. La contraseña debe tener al menos dos símbolos de estos: *, _, @, &, /, # ")
print("6. La contraseña debe tener al menos un número mayor o igual a 6. ")
print("-------------------------------------------------------------------------------------------------")

#Inicializamos las variables que no están dentro del bucle. 
correctas = 0
incorrectas = 0

#Empezamos el bucle que hará que el usuario pueda introducir 3 contraseñas diferentes. 
for veces in range(3):

    #Inicializamos las variables necesarias...
    password = input("Introduce la contraseña: ")

    condicion1 = 0
    condicion2 = 0
    condicion3 = 0
    condicion4 = 0
    condicion5 = 0

    longitud = len(password)

    #Y, para empezar, comprobamos si la longitud es la adecuada. 
    #Si no es así, nos saltamos todas las comprobaciones. 
    if not (longitud >= 6 and longitud <= 8):
        print(f"La longitud de tu contraseña es de {longitud}, así que no cumple con los requisitos. ")
        incorrectas += 1
    else:

        #Empezamos las comprobaciones teniendo en cuenta la longitud de la contraseña. 
        for i in range(longitud):

            #Asignamos la letra correspondiente a una variable para simplificar el proceso...
            letra = password[i]
            
            for condicion in range(5):
                
                #Y empezamos con las comprobaciones. 
                #En cada caso, se lleva la cuenta en una variable específica. 
                if condicion == 0:
                    if letra.isdigit():
                        if int(letra) <= 5 and int(letra) >= 1:
                            condicion1 += 1
                
                if condicion == 1:
                    if letra.isalpha():
                        if letra.islower() == True:
                            condicion2 += 1
                
                if condicion == 2:
                    if letra.isalpha() == True:
                        if letra.isupper() == True:
                            condicion3 += 1
                
                if condicion == 3:
                    if letra in "*_@&/#":
                        condicion4 += 1
                
                if condicion == 4:
                    if letra.isdigit() == True:
                        if int(letra) >= 6:
                            condicion5 += 1

        #Una vez acabamos con las comprobaciones, vemos si todas las condiciones se han cumplido. 
        #Dependiendo de el caso, mostramos un mensaje u otro y sumamos la cuenta de las correctas o incorrectas. 
        if condicion1 >= 2 and condicion2 >= 2 and condicion3 >= 1 and condicion4 >= 2 and condicion5 >= 1:
            correctas += 1
            print(f"El formato de la contraseña {veces + 1} es correcto. ¡Felicidades! ")
        else:
            incorrectas += 1
            print(f"El formato de la contraseña {veces + 1} es incorrecto. ¡Vuelve a intentarlo! ")

#Una vez ha introducido las tres contraseñas, mostramos un resumen final. 
print(f"Ya has introducido {veces + 1} contraseñas, así que has acabado el programa. ")
print(f"Has introducido {correctas} contraseñas correctas. ")
print(f"Has introducido {incorrectas} contraseñas incorrectas. ")

#TESTEOS:
#CONTRASEÑA     -     SALIDA

#1. a1b2C@#     -     El formato de la contraseña 1 es incorrecto. ¡Vuelve a intentarlo!
#2. 2iM4*z/7    -     El formato de la contraseña 1 es correcto. ¡Felicidades! 
#3. IM7d/6l     -     El formato de la contraseña 2 es incorrecto. ¡Vuelve a intentarlo!
#4. 3O7nl4//_,  -     La longitud de tu contraseña es de 10, así que no cumple con los requisitos. 
#5. 23uoV*#9    -     El formato de la contraseña 2 es correcto. ¡Felicidades!
#6. 99io*/55    -     El formato de la contraseña 3 es incorrecto. ¡Vuelve a intentarlo!
#7. z95Lp&1@    -     El formato de la contraseña 1 es correcto. ¡Felicidades! 
#8. Lm&91/M3    -     El formato de la contraseña 2 es incorrecto. ¡Vuelve a intentarlo! 
#9. 8j_kL       -     La longitud de tu contraseña es de 5, así que no cumple con los requisitos. 
#10. _K7o2p1_   -     El formato de la contraseña 1 es correcto. ¡Felicidades!