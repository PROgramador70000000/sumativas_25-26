#4. Realiza un programa donde un usuario escoja a partir del siguiente menú, la opción que corresponda al combustible que desea para repostar su vehículo (1, 2, 3, 4)

#Primero mostramos el mensaje de la gasolinera, con los diferentes tipos de gasoil. 
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("2. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")

#Y luego los diferentes precios para orientar al comprador antes de elegir un tipo. 
print("****PRECIOS COMBUSTIBLES****")
print("Sin plomo 95 - 1.765 €/litro")
print("Sin plomo 98 - 1.913 €/litro")
print("Gasóleo A - 1.746 €/litro")
print("Gasóleo A+ - 1.839 €/litro")

#Inicializamos descuento a 0 para más tarde comprobar si hay descuento o no. 
descuento = 0

#Y finalmente le pedimos al comprador el tipo de gasolina que quiere comprar y cuantos litros va a consumir. 
gasolina = int(input("Escoja el tipo de combustible (número): "))
litros = float(input("Introduzca el número de litros a repostar: "))

#Calculamos el precio sin descuentos, para cada tipo de gasolina. 
if gasolina == 1:
    total = litros * 1.765
elif gasolina == 2:
    total = litros * 1.913
elif gasolina == 3:
    total = litros * 1.746
elif gasolina == 4:
    total = litros * 1.839

#Y ahora aplicamos el descuento en una variable distinta (si lo hay). 
if gasolina == 2:
    descuento = total - (total / 10)
if gasolina == 4:
    descuento = total - ((total / 100) * 12)

#Con un simple condicional detectamos si se ha aplicado un descuento. y en función de ese factor mostramos un mensaje u otro. 
if descuento == 0:
    print("El total a pagar es de", total, "euros. ")
else: 
    print("El total a pagar es de", total, "euros, pero con el descuento se queda en", descuento, "euros. ")