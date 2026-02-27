#Importamos las librerías necesarias. 
import random
import time

#Definimos las variables que no se reinician en cada partida.
otra = 's'
inicio = time.time()
ahorcado = ['A', 'H', 'O', 'R', 'C', 'A', 'D', 'O']
normal = 'aeiouAEIOU'
tildes = 'áéíóúÁÉÍÓÚ'

lista_palabrasecreta = ['pátata']
apuestas = 'n'
dinero = 200

apuestas = input('¿Quieres jugar con apuestas? (s/n): ')
if not apuestas in 'nNsS':
    print('Introduce una respuesta válida (s/n).')
    while not apuestas in 'nNsS':
        apuestas = input('¿Quieres jugar con apuestas? (s/n): ')
        if not apuestas in 'nNsS':
            print('Introduce una respuesta válida (s/n).')

if apuestas in 'nN':
        print('¡Perfecto! Empezamos el juego sin apuestas. ')
elif apuestas in 'sS':
    print('Vale, vamos a jugar con apuestas. En este modo, ganarás o perderás dinero dependiendo de si ganas o pierdes. ')
    print('Vamos a jugar al ahorcado. Dependiendo de la dificultad de la palabra, ganarás o perderás más dinero. ')
    print('Empiezas con 200 euros. ¡Buena suerte!')
    
#Definimos las funciones que necesitaremos más adelante. 
def imprimir_partida():
    #Esta función muestra el estado de la partida; los guiones y letras acertadas en la palabra secreta. 
    #Ahora hacemos lo mismo tres veces; asignamos variable vacía, y le concatenamos todos los elementos de la lista correspondiente. 
    salida = ''
    for i in range(len(lista_partida)):
        salida = salida + lista_partida[i] + ' '
    aciertos = ''
    for i in range(len(lista_aciertos)):
        aciertos = aciertos + lista_aciertos[i] + ' '
    fallos = ''
    for i in range(len(lista_errores)):
        fallos = fallos + lista_errores[i] + ' '
    #Por último, mostramos el estado de la partida, y las letras acertadas y erróneas.
    print(salida)
    print(f'Letras acertadas: {aciertos}')
    print(f'Letras erróneas: {fallos}')

def comprobar_letra(respuesta):
    #Esta función comprueba si la letra está en la palabra, y si es así actualiza la partida. 
    #Primero comprobamos si la letra tiene tilde, y si es así la cambiamos por su equivalente sin tilde.
    #Gracias a las variables 'normal' y 'tildes' que hemos asignado antes. 
    if respuesta in tildes and tilde == True:
        respuesta = normal[tildes.index(respuesta)]
    #Palabradef es una versión de la palabra secreta sin tildes. 
    if respuesta in palabradef:
        for i in range(len(palabradef)):
        #Este bucle actualiza la lista de partida, en caso de que se haya acertado una letra. 
            if palabradef[i] == respuesta:
                lista_partida[i] = palabra[i]
        print('¡Muy bien! Has acertado una letra.')
        lista_aciertos.append(respuesta)
    else:
        #Si la letra no está en la palabra secreta, se añade a la lista de ahorcado la letra correspondiente...
        #Con el ingenioso método de tomar la letra con índice de la longitud de la lista. 
        lista_ahorcado.append(ahorcado[len(lista_ahorcado)])
        print('¡Oh no! Esa letra no está en la palabra secreta.')
        lista_errores.append(respuesta)
        print(lista_ahorcado)

while otra in 'sS' and len(lista_palabrasecreta) > 0 and apuestas in 'nN':
    #Entramos en el Bucle. Solo saldremos si no queremos jugar más o si no quedan más palabras secretas.
    #Se inicializan las variables que sí se reinician en cada partida.
    lista_partida = []
    lista_ahorcado = []
    palabra = random.choice(lista_palabrasecreta)
    lista_aciertos = []
    lista_errores = []
    tilde = False

    #Si la palabra secreta tiene tildes, se crea otra variable que guarda una versión sin tildes. 
    for i in range(len(palabra)):
        if palabra[i] in tildes:
            palabradef = palabra.replace(palabra[i], normal[tildes.index(palabra[i])])
            tilde = True
    if not tilde:
        palabradef = palabra   

    #Se crea la lista de partida, con tantos guiones como letras tenga la palabra secreta.
    for i in range(len(palabradef)):
        lista_partida.append('_')

    #Ahora sí, empezamos con el juego. Mostramos las instrucciones del programa. 
    print('JUEGO DEL AHORCADO')
    print('Vas a tener que acertar la palabra secreta, letra a letra. Tienes 8 intentos para adivinarla. ')
    print('Introduce \'palabra\' para intentar adivinar la palabra secreta de una vez. ¡Pero cuidado! Si fallas, perderás automáticamente.')
    print('¡Buena suerte!')
    respuesta = ''
    respuesta_definitiva = ''

    #Entramos en la partida. No saldremos hasta que hayamos acertado o hayamos perdido.
    while respuesta_definitiva != palabradef and respuesta_definitiva != palabra and len(lista_ahorcado) < 8:
        imprimir_partida()
        respuesta = input('Introduce una letra: ')
        if respuesta == 'palabra':
            #Primero, comprobamos si el jugador quiere averiguar la palabra secreta. 
            #Con una variable (introducir_palabra), evitamos errores y bucles innecesarios. 
            respuesta = input('Introduce la palabra secreta: ')
            if respuesta == palabradef or respuesta == palabra:
                respuesta_definitiva = palabradef
                introducir_palabra = True
            else:
                print('¡Oh no! Esa no es la palabra secreta. Has perdido automáticamente.')
                lista_ahorcado = ahorcado
                introducir_palabra = True
        else:
            introducir_palabra = False

        if respuesta in lista_aciertos:
            #Se comprueba si la letra ya había sido acertada. 
            print('¡Ya has acertado esa letra! Intenta con otra diferente.')
            while respuesta in lista_aciertos:
                respuesta = input('Introduce una letra: ')
                if respuesta in lista_aciertos:
                    print('¡Ya has acertado esa letra! Intenta con otra diferente.')

        if respuesta in lista_errores:
            #Se comprueba si la letra ya había sido errónea. 
            print('¡Ya has fallado esa letra! Intenta con otra diferente.')
            while respuesta in lista_errores:
                respuesta = input('Introduce una letra: ')
                if respuesta in lista_errores:
                    print('¡Ya has fallado esa letra! Intenta con otra diferente.')

        if len(respuesta) == 1 and introducir_palabra == False:
            #En caso de que la letra tenga la longitud correcta, se comprueba si está en la palabra secreta.
            comprobar_letra(respuesta)
        elif introducir_palabra == False:
            #En caso contrario, se pide una nueva letra hasta que introduzca una letra o la palabra secreta.
            print('¡Error! Solo puedes introducir una letra a la vez.')
            while len(respuesta) != 1 and respuesta != 'palabra':
                respuesta = input('Introduce una letra: ')
                if len(respuesta) != 1 and respuesta != 'palabra':
                    print('¡Error! Solo puedes introducir una letra a la vez.')
            if len(respuesta) == 1:
                comprobar_letra(respuesta)
            elif respuesta == 'palabra':
                respuesta = input('Introduce la palabra secreta: ')
                if respuesta == palabradef or respuesta == palabra:
                    respuesta_definitiva = palabradef
                    introducir_palabra = True
                else:
                    print('¡Oh no! Esa no es la palabra secreta. Has perdido automáticamente.')
                    lista_ahorcado = ahorcado
                introducir_palabra = True
        
        #Por último, se actualiza la respuesta definitiva, para comprobar si el jugador ha ganado o continua jugando.
        if introducir_palabra == False:
            respuesta_definitiva = ''
            for i in range(len(lista_partida)):
                respuesta_definitiva = respuesta_definitiva + lista_partida[i]

    #Una vez hemos acabado con la paryida, se muestra la partida una última vez...
    if introducir_palabra == False:
        imprimir_partida()

    #Y se muestra un mensaje dependiendo de si el jugador ha ganaod o perdido. 
    if respuesta_definitiva == palabradef or respuesta_definitiva == palabra:
        print(f'¡Enhorabuena! Has adivinado la palabra secreta: {palabra}.')
    else:
        print(f'¡Lo siento! Has perdido. La palabra secreta era: {palabra}.')
    if introducir_palabra == False:
        print(f'Has acertado {len(lista_aciertos)} letras y has cometido {len(lista_errores)} errores.')

    #Se elimina la palabra utilizada de la lista, para que no vuelva a aparecer. 
    lista_palabrasecreta.remove(palabra)

    #Se le da la opción al jugador de añadir una palabra al juego con un código batsante sencillo. 
    añadir = input('¿Quieres añadir una palabra al juego? (s/n): ')
    if añadir in 'sSnN':
        if añadir in 'sS':
            nueva_palabra = input('Introduce la palabra que quieres añadir: ')
            lista_palabrasecreta.append(nueva_palabra)
            print(f'¡Gracias por tu aportación! La palabra "{nueva_palabra}" se ha añadido al juego.')
    else: 
        #Como siempre, tenemos en cuenta si se introduce una respuesta inválida. 
        print('Introduce una respuesta válida (s/n).')
        while not añadir in 'sSnN':
            añadir = input('¿Quieres añadir una palabra al juego? (s/n): ')
            if añadir in 'sSnN':
                if añadir in 'sS':
                    nueva_palabra = input('Introduce la palabra que quieres añadir: ')
                    lista_palabrasecreta.append(nueva_palabra)
                    print(f'¡Gracias por tu aportación! La palabra "{nueva_palabra}" se ha añadido al juego.')
            else: 
                print('Introduce una respuesta válida (s/n).')

    #Por último, se da la opción de jugar otra vez, teniendo en cuenta si se introduce una respuesta inválida.
    otra = input('¿Quieres jugar otra vez? (s/n): ')
    if not otra in 'sSnN':
        print('Introduce una respuesta válida (s/n).')
        while not otra in 'sSnN':
            otra = input('¿Quieres jugar otra vez? (s/n): ')
            if not otra in 'sSnN':
                print('Introduce una respuesta válida (s/n).')

if apuestas in 'nN':
    #Una vez el juego ha acabado, se muestra un mensaje de despedida, y el tiempo total de juego.
    if otra in 'nN':
        print('Fin del programa. ¡Gracias por jugar! ')
    else:
        print('Ya no quedan más palabras secretas. ¡Gracias por jugar! ')

print(f'Tiempo total de juego: {time.time() - inicio:.2f} segundos.')