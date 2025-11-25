#Primero, asignamos a una variable un valor en blanco, para luego poder encadenar valores en ella sin tener ningún problema. 
contraseña_segura = ""

#Le decimos al usuario las instrucciones para crear su conraseña segura. 
print("INSTRUCCIONES: ")
print("1. La contraseña debe tener entre 6 y 8 dígitos. ")
print("2. Tendrá que poner los siguientes valores en la posición indicada: ")
print("Posición 1. Un número mayor o igual a 1 y menor o igual a 5. ")
print("Posición 2. Una letra minúscula. ")
print("Posición 3. Una letra mayúscula. ")
print("Posición 4. Uno de los siguientes símbolos: *, _, @. ")
print("Posición 5. Una letra minúscula. ")
print("Posición 6. Un número mayor o igual a 6 y menor o igual a 9. ")
print("Posición 7. Uno de los siguientes símbolos: &, /, #. ")
print("Posición 8. Un número menor o igual a 5.”")

#Asignamos a una variable la contraseña que elige el jugador. 
contraseña = str(input("Introduzca la contraseña elegida, por favor. "))

#Para empezar, comprobamos si la longitud de la contraseña es correcta, y en caso contrario mostramos un mensaje por pantalla y acabamos el programa. 
if not (len(contraseña) <= 8 and len(contraseña) >= 6):
    print("Error, la contraseña tiene una longitud de", len(contraseña), "caracteres y no cumple con los requisitos. ")
    exit()

#Y ahora, carácter por carácter, comprobamos si los requisitos han sido cumplimos. 
#En cada caso, comprobamos la opción negativa, y si es así añadimos a la variable en blanco un texto diciendo que hay un error en el carácter que toque. 
#Si el carácter es correcto, simplemente pasará al sguiente condicional. 
if not (contraseña[0].isdigit() and (int(contraseña[0]) <= 5 and int(contraseña[0]) >= 1)):
    contraseña_segura = contraseña_segura + "Error en el carácter 1. "

if not (contraseña[1].isalpha() and (str(contraseña[1])).islower()):
    contraseña_segura = contraseña_segura + "Error en el carácter 2. "

if not (contraseña[2].isalpha() and (str(contraseña[2])).isupper()):
    contraseña_segura = contraseña_segura + "Error en el carácter 3. "

if not (contraseña[3] == "*" or contraseña[3] == "_" or contraseña[3] == "@"):
    contraseña_segura = contraseña_segura + "Error en el carácter 4. "

if not (contraseña[4].isalpha() and (str(contraseña[4])).islower()):
    contraseña_segura = contraseña_segura + "Error en el carácter 5. "

if not (contraseña[5].isdigit() and (int(contraseña[5])) <= 9 and (int(contraseña[5])) >= 6):
    contraseña_segura = contraseña_segura + "Error en el carácter 6. "

if len(contraseña) >= 7:
    if not (contraseña[6] == "&" or contraseña[6] == "/" or contraseña[6] == "#"):
        contraseña_segura = contraseña_segura + "Error en el carácter 7. "

if len(contraseña) == 8:
    if not (contraseña[7].isdigit() and (int(contraseña[7])) <= 5):
        contraseña_segura = contraseña_segura + "Error en el carácter 8. "

#Por último, si la variable que estaba en blanco al principio sigue en blanco, significa que la contraeña es correcta. Si no, mostramos la variable. ¡Listo!
if not contraseña_segura == "":
    print(contraseña_segura)
else:
    print("El formato de CONTRASEÑA es correcto. ")