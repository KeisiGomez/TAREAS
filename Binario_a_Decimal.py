binario = input("Dame un numero binario: ")
decimal = 0
longitud = len(binario)
contador = 0
binario_rev = binario[::-1]
while contador < longitud:
    if binario_rev[contador] == "1":
        decimal += 2**contador
    contador +=1

print(decimal)