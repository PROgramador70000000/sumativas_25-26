import random
import time

otra = 's'
inicio = time.time()
ahorcado = ['A', 'H', 'O', 'R', 'C', 'A', 'D', 'O']
jugadores = int(input('¿Cuántos jugadores van a jugar? (1 o 2): '))

if jugadores != 1 and jugadores != 2:
    while jugadores != 1 and jugadores != 2:
        jugadores = int(input('Respuesta inválida. ¿Cuántos jugadores van a jugar? (1 o 2): '))

if jugadores == 1:
    lista_palabrasecreta = ['rahez', 'petricor', 'hoz', 'exacerbar', 'contumaz', 'whiskey', 'hipopotomonstrosesquipedaliofobia', 'inmarcesible', 'orondo', 'ñañara', 'zurriburri', 'ful']

    def imprimir_partida():
        salida = ''
        for i in range(len(lista_partida)):
            salida = salida + lista_partida[i] + ' '
        aciertos = ''
        for i in range(len(lista_aciertos)):
            aciertos = aciertos + lista_aciertos[i] + ' '
        fallos = ''
        for i in range(len(lista_errores)):
            fallos = fallos + lista_errores[i] + ' '
        print(salida)
        print(f'Letras acertadas: {aciertos}')
        print(f'Letras erróneas: {fallos}')

    def comprobar_letra(respuesta):
        if respuesta in palabra:
            for i in range(len(palabra)):
                if palabra[i] == respuesta:
                    lista_partida[i] = respuesta
            print('¡Muy bien! Has acertado una letra.')
            lista_aciertos.append(respuesta)
        else:
            lista_ahorcado.append(ahorcado[len(lista_ahorcado)])
            print('¡Oh no! Esa letra no está en la palabra secreta.')
            lista_errores.append(respuesta)
            print(lista_ahorcado)

    while otra in 'sS' and len(lista_palabrasecreta) > 0:
        lista_partida = []
        lista_ahorcado = []
        palabra = random.choice(lista_palabrasecreta)
        lista_aciertos = []
        lista_errores = []

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
        print(f'Has acertado {len(lista_aciertos)} letras y has cometido {len(lista_errores)} errores.')

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

elif jugadores == 2:
    while otra in 'sS':

        def imprimir_partida1():
            salida = ''
            for i in range(len(lista_partida1)):
                salida = salida + lista_partida1[i] + ' '
            aciertos = ''
            for i in range(len(lista_aciertos1)):
                aciertos = aciertos + lista_aciertos1[i] + ' '
            fallos = ''
            for i in range(len(lista_errores1)):
                fallos = fallos + lista_errores1[i] + ' '
            print(salida)
            print(f'Letras acertadas: {aciertos}')
            print(f'Letras erróneas: {fallos}')

        def comprobar_letra1(respuesta):
            if respuesta in palabra1:
                for i in range(len(palabra1)):
                    if palabra1[i] == respuesta:
                        lista_partida1[i] = respuesta
                print('¡Muy bien! Has acertado una letra.')
                lista_aciertos1.append(respuesta)
            else:
                lista_ahorcado1.append(ahorcado[len(lista_ahorcado1)])
                print('¡Oh no! Esa letra no está en la palabra secreta.')
                lista_errores1.append(respuesta)
                print(lista_ahorcado1)

        def imprimir_partida2():
            salida = ''
            for i in range(len(lista_partida2)):
                salida = salida + lista_partida2[i] + ' '
            aciertos = ''
            for i in range(len(lista_aciertos2)):
                aciertos = aciertos + lista_aciertos2[i] + ' '
            fallos = ''
            for i in range(len(lista_errores2)):
                fallos = fallos + lista_errores2[i] + ' '
            print(salida)
            print(f'Letras acertadas: {aciertos}')
            print(f'Letras erróneas: {fallos}')

        def comprobar_letra2(respuesta):
            if respuesta in palabra2:
                for i in range(len(palabra2)):
                    if palabra2[i] == respuesta:
                        lista_partida2[i] = respuesta
                print('¡Muy bien! Has acertado una letra.')
                lista_aciertos2.append(respuesta)
            else:
                lista_ahorcado2.append(ahorcado[len(lista_ahorcado2)])
                print('¡Oh no! Esa letra no está en la palabra secreta.')
                lista_errores2.append(respuesta)
                print(lista_ahorcado2)

        jugador1 = input('Jugador 1, introduce tu nombre: ')
        jugador2 = input('Jugador 2, introduce tu nombre: ')
        print('¡Empecemos! En el modo de dos jugadores, cada uno eligirá la palabra secreta del otro. ')
        print('Cada uno tenéis 8 intentos, que se mostrarán con las letras de la palabra "AHORCADO". ¡Buena suerte!')
        palabra1 = input(f'{jugador1}, introduce la palabra secreta para {jugador2}: ')
        palabra2 = input(f'{jugador2}, introduce la palabra secreta para {jugador1}: ')

        lista_partida1 = []
        lista_partida2 = []
        lista_ahorcado1 = []
        lista_ahorcado2 = []
        lista_aciertos1 = []
        lista_aciertos2 = []
        lista_errores1 = []
        lista_errores2 = []

        respuesta_definitiva1 = ''
        respuesta_definitiva2 = ''
        turno = 1

        while respuesta_definitiva1 != palabra1 and len(lista_ahorcado1) < 8 and respuesta_definitiva2 != palabra2 and len(lista_ahorcado2) < 8:
            if turno == 1:
                respuesta = input(f'Turno de {jugador1}. Introduce una letra: ')
                if len(respuesta) == 1:
                    comprobar_letra1(respuesta)
                    imprimir_partida1()
                else:
                    print('¡Error! Solo puedes introducir una letra a la vez.')
                    while len(respuesta) != 1:
                        respuesta = input(f'Turno de {jugador1}. Introduce una letra: ')
                        if len(respuesta) != 1:
                            print('¡Error! Solo puedes introducir una letra a la vez.')
                    comprobar_letra1(respuesta)
                    imprimir_partida1()
                respuesta_definitiva1 = ''
                for i in range(len(lista_partida1)):
                    respuesta_definitiva1 = respuesta_definitiva1 + lista_partida1[i]
                turno = 2
            elif turno == 2:
                respuesta = input(f'Turno de {jugador2}. Introduce una letra: ')
                if len(respuesta) == 1:
                    comprobar_letra2(respuesta)
                    imprimir_partida2()
                else:
                    print('¡Error! Solo puedes introducir una letra a la vez.')
                    while len(respuesta) != 1:
                        respuesta = input(f'Turno de {jugador2}. Introduce una letra: ')
                        if len(respuesta) != 1:
                            print('¡Error! Solo puedes introducir una letra a la vez.')
                    comprobar_letra2(respuesta)
                    imprimir_partida2()
                respuesta_definitiva2 = ''
                for i in range(len(lista_partida2)):
                    respuesta_definitiva2 = respuesta_definitiva2 + lista_partida2[i]
                turno = 1


print('Fin del programa. ¡Gracias por jugar! ')
print(f'Tiempo total de juego: {time.time() - inicio:.2f} segundos.')
