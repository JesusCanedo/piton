#print("hola");
#print("adios");

# numero = int(input("Ingresa un número: "))

# if numero > 5:
#     print("El número es mayor que 5:", numero)
# else:
#     print("El número no es mayor que 5:", numero)

# i = 0
# for i in range(5):
#     print(i)

numeros = [5, 4.23, 3.56, 2, 1]

print("contenido: ", numeros)
print("tamaño: ", len(numeros))
del numeros[3]
print("primer elemento: ", numeros[0])
numeros[-1] = numeros[2]
print("ultimo elemento: ", numeros[-1])

formato = []

for x in numeros:
    formato.append(x)

print(formato)

total = 0
for i in numeros:
    total += i

print("total: ", total)

