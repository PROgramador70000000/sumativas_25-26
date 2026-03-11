#Importamos las librerías necesarias. 
import random
import time
import os

#Definimos las variables que no se reinician en cada partida.
otra = 's'
inicio = time.time()
ahorcado = ['A', 'H', 'O', 'R', 'C', 'A', 'D', 'O']
normal = 'aeiouAEIOU'
tildes = 'áéíóúÁÉÍÓÚ'

lista_palabrasecreta = palabras = [
    "casa", "perro", "gato", "árbol", "cielo", "camino", "fuego", "agua", "tierra",
    "viento", "luz", "sombra", "noche", "día", "sol", "luna", "estrella", "flor",
    "hoja", "mar", "río", "montaña", "valle", "ciudad", "pueblo", "bosque", "campo",
    "nube", "tormenta", "lluvia", "trueno", "relámpago", "brisa", "arena", "playa",
    "costa", "isla", "océano", "barco", "puerto", "puente", "carretera", "coche",
    "tren", "avión", "bicicleta", "camión", "persona", "niño", "niña", "hombre",
    "mujer", "amigo", "amiga", "familia", "madre", "padre", "hermano", "hermana",
    "abuelo", "abuela", "tío", "tía", "primo", "prima", "profesor", "profesora",
    "alumno", "alumna", "escuela", "libro", "cuaderno", "lápiz", "bolígrafo",
    "mesa", "silla", "puerta", "ventana", "pared", "techo", "suelo", "computadora",
    "pantalla", "ratón", "teclado", "internet", "programa", "código", "juego",
    "música", "película", "arte", "pintura", "escultura", "canción", "idioma",
    "palabra", "frase", "texto", "historia", "cultura", "ciencia", "matemáticas",
    "física", "química", "biología", "universo", "planeta", "galaxia", "energía",
    "átomo", "molécula", "célula", "animal", "planta", "insecto", "pez", "ave",
    "mamífero", "reptil", "anfibio", "comida", "bebida", "pan", "leche", "carne",
    "fruta", "verdura", "arroz", "pasta", "sal", "azúcar", "aceite", "huevo",
    "queso", "tomate", "patata", "zanahoria", "manzana", "naranja", "plátano",
    "uva", "melón", "sandía", "fresa", "cereza", "limón", "pera", "durazno",
    "café", "té", "chocolate", "galleta", "pastel", "helado", "sopa", "ensalada",
    "pollo", "pescado", "cerdo", "vaca", "oveja", "caballo", "burro", "conejo",
    "tigre", "león", "elefante", "jirafa", "mono", "zorro", "lobo", "oso",
    "serpiente", "águila", "halcón", "paloma", "gallina", "pato", "ganso",
    "mariposa", "abeja", "hormiga", "araña", "caracol", "cangrejo", "delfín",
    "ballena", "tiburón", "pulpo", "medusa", "estrella", "roca", "piedra",
    "metal", "madera", "plástico", "vidrio", "papel", "tela", "cuero", "oro",
    "plata", "cobre", "hierro", "acero", "diamante", "rubí", "esmeralda",
    "montaña", "colina", "acantilado", "desierto", "selva", "pradera",
    "volcán", "glaciar", "laguna", "pantano", "cascada", "río", "arroyo",
    "laguna", "bahía", "golfo", "océano", "mar", "playa", "duna", "cueva",
    "gruta", "caverna", "templo", "iglesia", "catedral", "mezquita", "sinagoga",
    "castillo", "palacio", "torre", "muralla", "fortaleza", "puente", "túnel",
    "edificio", "rascacielos", "hotel", "hospital", "mercado", "tienda",
    "supermercado", "restaurante", "cafetería", "parque", "plaza", "jardín",
    "fuente", "estatua", "museo", "teatro", "cine", "estadio", "gimnasio",
    "piscina", "biblioteca", "oficina", "fábrica", "almacén", "aeropuerto",
    "estación", "terminal", "puerto", "garaje", "cocina", "baño", "dormitorio",
    "salón", "comedor", "pasillo", "balcón", "terraza", "jardín", "patio",
    "sótano", "ático", "ventilador", "calefacción", "aire", "humo", "fuego",
    "ceniza", "carbón", "gas", "electricidad", "motor", "máquina", "herramienta",
    "martillo", "destornillador", "llave", "sierra", "taladro", "tornillo",
    "tuerca", "clavo", "cuerda", "cadena", "candado", "puerta", "ventana",
    "espejo", "reloj", "teléfono", "radio", "televisión", "cámara", "foto",
    "vídeo", "película", "documento", "archivo", "carpeta", "correo", "mensaje",
    "señal", "símbolo", "mapa", "planeta", "continente", "país", "región",
    "provincia", "ciudad", "pueblo", "barrio", "calle", "avenida", "carretera",
    "camino", "sendero", "ruta", "viaje", "turismo", "aventura", "exploración",
    "trabajo", "empleo", "oficio", "profesión", "arte", "ciencia", "deporte",
    "juego", "competición", "carrera", "salud", "enfermedad", "medicina",
    "doctor", "enfermero", "paciente", "cura", "remedio", "vacuna", "virus",
    "bacteria", "energía", "fuerza", "velocidad", "tiempo", "espacio", "materia",
    "forma", "color", "tamaño", "peso", "altura", "anchura", "profundidad"
]

apuestas = 'n'

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

def guardar_partida():
    with open('ultima_partida.txt', 'w') as archivo:
        archivo.write(f'{time.ctime()};')
        archivo.write(f'{palabra};')
        archivo.write(f'{len(lista_aciertos)};')
        archivo.write(f'{len(lista_errores)};')
        if respuesta_definitiva == palabradef or respuesta_definitiva == palabra:
            archivo.write('Victoria\n')
        else:
            archivo.write('Derrota\n')

if os.path.exists('ultima_partida.txt'):
    if os.path.getsize('ultima_partida.txt') > 0:
        mostrar_partida = input('Hay una partida guardada. ¿Quieres ver el resumen? (s/n): ')
        if not mostrar_partida in 'sSnN':
            print('Introduce una respuesta válida (s/n).')
            while not mostrar_partida in 'sSnN':
                mostrar_partida = input('Hay una partida guardada. ¿Quieres ver el resumen? (s/n): ')
                if not mostrar_partida in 'sSnN':
                    print('Introduce una respuesta válida (s/n).')
        if mostrar_partida in 'sS':
            with open('ultima_partida.txt', 'r') as archivo:
                partida_guardada = archivo.read().split(';')
                print('Resumen de tu última partida:')
                print(f'Fecha y hora: {partida_guardada[0]}')
                print(f'Palabra secreta: {partida_guardada[1]}')
                print(f'Número de aciertos: {partida_guardada[2]}')
                print(f'Número de errores: {partida_guardada[3]}')
                print(f'Resultado: {partida_guardada[4]}')

apuestas = input('¿Quieres jugar con apuestas? No podrás cambiar esto más tarde. (s/n): ')
if not apuestas in 'nNsS':
    print('Introduce una respuesta válida (s/n).')
    while not apuestas in 'nNsS':
        apuestas = input('¿Quieres jugar con apuestas? No podrás cambiar esto más tarde. (s/n): ')
        if not apuestas in 'nNsS':
            print('Introduce una respuesta válida (s/n).')

if apuestas in 'nN':
        print('¡Perfecto! Empezamos el juego sin apuestas. ')
elif apuestas in 'sS':
    #El modo con apuestas es básicamente ina copia del original con solo unos cuantos cambios. 
    #Me pregunto si es posible hacer el modo de apuestas sin repetirlo todo, pero no se me ocurre. 
    print('Vale, vamos a jugar con apuestas. En este modo, ganarás o perderás dinero dependiendo de si ganas o pierdes. ')
    print('Vamos a jugar al ahorcado. Dependiendo de la dificultad de la palabra, ganarás o perderás más dinero. ')
    print('Empiezas con 200 euros. ¡Buena suerte!')
    dinero = 200
    palabras_faciles = ['pato', 'gato', 'casa', 'perro', 'árbol', 'libro', 'coche', 'mesa', 'silla', 'ventana']
    palabras_medio = ['pelota', 'camisa', 'zapato', 'ciudad', 'playa', 'montaña', 'río', 'mariposa', 'avión', 'estrella']
    palabras_dificiles = ['orondo', 'hoz', 'exacerbar', 'zozobro', 'inmarcesible', 'petricor', 'hipopotomonstrosesquipedaliofobia', 'zorzal', 'yuxtaposición', 'jirafa', 'píxel', 'pneumonoultramicroscopicsilicovolcanoconiosis']

    while otra in 'sS' and apuestas in 'sS' and len(palabras_dificiles) > 0 and len(palabras_faciles) > 0 and len(palabras_medio) > 0 and dinero > 0:
        print(f'Tienes {dinero} euros. ')
        apuesta = input('¿Cuánto quieres apostar? Máximo 500 euros: ')
        if int(apuesta) > dinero:
            print(f'No puedes apostar más de lo que tienes. Tienes {dinero} euros.')
            while int(apuesta) > dinero:
                apuesta = input('¿Cuánto quieres apostar? Máximo 500 euros: ')
                if int(apuesta) > dinero:
                    print(f'No puedes apostar más de lo que tienes. Tienes {dinero} euros.')
        if not apuesta.isdigit() or int(apuesta) < 0 or int(apuesta) > 500:
            print('Introduce una cantidad válida (0-500 euros).')
            while not apuesta.isdigit() or int(apuesta) < 0 or int(apuesta) > 500:
                apuesta = input('¿Cuánto quieres apostar? Máximo 500 euros: ')
                if not apuesta.isdigit() or int(apuesta) < 0 or int(apuesta) > 500:
                    print('Introduce una cantidad válida (0-500 euros).')

        if int(apuesta) <= 20:
            print('Has elegido apostar poco. La palabra secreta será fácil. ')
            lista_palabrasecreta = palabras_faciles
        elif int(apuesta) <= 100:
            print('Has elegido apostar una cantidad media. La palabra secreta será de dificultad media. ')
            lista_palabrasecreta = palabras_medio
        else:
            print('Has elegido apostar mucho. La palabra secreta será difícil. ')
            lista_palabrasecreta = palabras_dificiles

        lista_partida = []
        lista_ahorcado = []
        palabra = random.choice(lista_palabrasecreta)
        lista_aciertos = []
        lista_errores = []
        tilde = False

        respuesta = ''
        respuesta_definitiva = ''

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
            print(f'Has ganado {apuesta} euros. Ahora tienes {dinero + int(apuesta)} euros.')
            dinero = dinero + int(apuesta)
        else:
            print(f'¡Lo siento! Has perdido. La palabra secreta era: {palabra}.')
            print(f'Has perdido {apuesta} euros. Ahora tienes {dinero - int(apuesta)} euros.')
            dinero = dinero - int(apuesta)
        if introducir_palabra == False:
            print(f'Has acertado {len(lista_aciertos)} letras y has cometido {len(lista_errores)} errores.')

        #Se elimina la palabra utilizada de la lista, para que no vuelva a aparecer. 
        lista_palabrasecreta.remove(palabra)

        otra = input('¿Quieres jugar otra vez? (s/n): ')
        if not otra in 'sSnN':
            print('Introduce una respuesta válida (s/n).')
            while not otra in 'sSnN':
                otra = input('¿Quieres jugar otra vez? (s/n): ')
                if not otra in 'sSnN':
                    print('Introduce una respuesta válida (s/n).')

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

if apuestas in 'sS':
    if otra in 'nN':
        print(f'Fin del programa. ¡Gracias por jugar! Tienes {dinero} euros. ')
    elif dinero <= 0:
        print('¡Oh no! Te has quedado sin dinero. Fin del programa. ¡Gracias por jugar!')
    else:
        print('Ya no quedan más palabras secretas. ¡Gracias por jugar!')

minutos = int((time.time() - inicio) // 60)
segundos = int((time.time() - inicio) % 60)

print(f'Tiempo total de juego: {minutos} minutos y {segundos} segundos.')

guardar = input('¿Quieres guardar un resumen de tu partida? (s/n): ')
if not guardar in 'sSnN':
    while not guardar in 'sSnN':
        print('Introduce una respuesta válida (s/n).')
        guardar = input('¿Quieres guardar un resumen de tu partida? (s/n): ')
        if not guardar in 'sSnN':
            print('Introduce una respuesta válida (s/n).')

if guardar in 'sS':
    guardar_partida()
    print('¡Partida guardada!')
else:
    print('¡Gracias por jugar!')