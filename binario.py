decimal = input()
binario = ""
cociente = int(decimal)
while cociente != 1 :
    residuo =  cociente % 2
    cociente = cociente // 2
    binario = binario + str(residuo)

binario = binario + str(residuo)
res = binario [::-1]
print(res)
