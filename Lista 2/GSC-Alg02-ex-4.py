x = int(input("Insira um número: "))
y = int(input("Insira um número: "))
z = int(input("Insira um número: "))

numeros = [x, y, z]

meio = (x+y+z) - (max(numeros)) - min(numeros)

print(min(numeros),meio,max(numeros))
