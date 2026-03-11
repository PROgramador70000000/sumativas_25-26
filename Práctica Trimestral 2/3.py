productos = input().split('-')
producto = []
precio = []
stock = []
for i in productos:
    producto.append(i.split(':')[0])
    precio.append(float(i.split(':')[1]))
    stock.append(int(i.split(':')[2]))