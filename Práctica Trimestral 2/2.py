contraseñas = input().split('-')
seguras = []
debiles = []
invalidas = []
len_max = ''
for i in contraseñas:
    numero = False
    letra = False
    especial = False
    len_err = False
    if len(i) > len(len_max):
        len_max = i
    if len(i) >= 8:
        len_err = True
    for j in i:
        if j.isdigit():
            numero = True
        elif j.isalpha():
            letra = True
        else:
            especial = True
    if numero and letra and not especial and len_err:
        seguras.append(i)
    elif especial:
        invalidas.append(i)
    else:
        debiles.append(i)
print(f'Contraseñas seguras: {len(seguras)}')
print(f'Contraseñas débiles: {len(debiles)}')
print(f'Contraseñas inválidas: {len(invalidas)}')
print(f'Contraseña más larga: {len_max}')