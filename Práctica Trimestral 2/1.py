numeros = input().split(', ')
print(numeros)
numeros.sort()
numeros.pop(0)
numeros.pop(len(numeros) - 1)
print(numeros)
for i in numeros:
    total += int(i)
media = total / len(numeros)
print(round(media, 2))
if media < 5:
    print('Rendimiento bajo. ')
elif media < 10:
    print('Rendimiento medio. ')
else:
    print('Rendimiento alto. ')