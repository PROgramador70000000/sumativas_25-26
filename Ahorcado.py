import random

otra = 's'

def imprimir_partida():
    salida = ''
    for i in range(len(lista_partida)):
        salida = salida + lista_partida[i] + ' '
    print(salida)

def comprobar_letra(respuesta):
    if respuesta in palabra:
        for i in range(len(palabra)):
            if palabra[i] == respuesta:
                lista_partida[i] = respuesta
        print('¡Muy bien! Has acertado una letra.')
    else:
        lista_ahorcado.append(ahorcado[len(lista_ahorcado)])
        print('¡Oh no! Esa letra no está en la palabra secreta.')
        print(lista_ahorcado)

while otra in 'sS':
    lista_palabrasecreta = ['perro', 'gato', 'casa', 'arbol', 'sol', 'luna', 'estrella', 'mariposa', 'avion', 'tren']
    lista_partida = []
    ahorcado = ['A', 'H', 'O', 'R', 'C', 'A', 'D', 'O']
    lista_ahorcado = []
    palabra = random.choice(lista_palabrasecreta)

    for i in range(len(palabra)):
        lista_partida.append('_')

    print('JUEGO DEL AHORCADO')
    print('Vas a tener que acertar la palabra secreta, letra a letra. Tienes 8 intentos para adivinarla. ')
    print('¡Buena suerte!')
    respuesta = ''
    respuesta_definitiva = ''
    while respuesta_definitiva != palabra and len(lista_ahorcado) < 8:
        imprimir_partida()
        respuesta = input('Introduce una letra: ')
        if len(respuesta) == 1:
            comprobar_letra(respuesta)
        else:
            print('¡Error! Solo puedes introducir una letra a la vez.')
            while len(respuesta) != 1:
                respuesta = input('Introduce una letra: ')
                if len(respuesta) != 1:
                    print('¡Error! Solo puedes introducir una letra a la vez.')
            comprobar_letra(respuesta)
        respuesta_definitiva = ''
        for i in range(len(lista_partida)):
            respuesta_definitiva = respuesta_definitiva + lista_partida[i]

    imprimir_partida()

    if respuesta_definitiva == palabra:
        print(f'¡Enhorabuena! Has adivinado la palabra secreta: {palabra}.')
    else:
        print(f'¡Lo siento! Has perdido. La palabra secreta era: {palabra}.')

    lista_palabrasecreta.remove(palabra)

    añadir = input('¿Quieres añadir una palabra al juego? (s/n): ')
    if añadir in 'sSnN':
        if añadir in 'sS':
            nueva_palabra = input('Introduce la palabra que quieres añadir: ')
            lista_palabrasecreta.append(nueva_palabra)
            print(f'¡Gracias por tu aportación! La palabra "{nueva_palabra}" se ha añadido al juego.')
    else: 
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

    otra = input('¿Quieres jugar otra vez? (s/n): ')
    if not otra in 'sSnN':
        print('Introduce una respuesta válida (s/n).')
        while not otra in 'sSnN':
            otra = input('¿Quieres jugar otra vez? (s/n): ')
            if not otra in 'sSnN':
                print('Introduce una respuesta válida (s/n).')