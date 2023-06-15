n      = 0
numero = int(input("Insira um número: "))
lista  = []
while n < numero:
    n += 1
    if numero%n == 0:
        lista.append(n)
print(f"Os divisores de {numero} são: {lista}")
