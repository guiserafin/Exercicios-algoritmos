"""Decimal para binário. Escreva um programa Python que converte um número decimal (base 10) para o
correspondente número binário (base 2). Leia o número decimal como um número inteiro fornecido pelo
usuário. Depois disso, use o algoritmo de divisão mostrado abaixo para fazer a conversão. Quando o
algoritmo terminar, a variável result contém a representação binária do número. Ao final exiba uma
mensagem informando o valor de result."""

result = ""
q = int(input("Escreva o número a ser convertido para binário: "))
while q != 0:
    r = q%2
    r = str(r)
    result = r + result
    q = q//2

print("O seu número em binário é: ", result)




