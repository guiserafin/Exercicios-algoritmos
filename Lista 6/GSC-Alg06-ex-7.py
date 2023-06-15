n = 0
numero = int(input("Insira um número: "))
lista = []
while n < numero:
    n +=1
    if numero%n == 0:
        lista.append(n)

resultado = 0
for i in range(0,len(lista)-1):
    resultado += lista[i]
print(f"Os divisores de {numero} são: {lista}")
if resultado == numero:
    print(f"O resultado da soma dos divisores é igual ao {numero} - É um número perfeito!!")
