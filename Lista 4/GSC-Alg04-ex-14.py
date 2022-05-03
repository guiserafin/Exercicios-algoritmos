"""Binário para decimal. Escreva um programa Python que converte um número binário (base 2) para
decimal (base 10). Seu programa deve iniciar lendo um número binário como uma string. Então, ele
deve computar o número decimal equivalente processando cada dígito do número binário. Finalmente
seu programa deve exibir uma mensagem informando o número decimal calculado."""

binario = input("Digite um número binário: ")

i = len(binario)
n = 0
decimal = 0
while i !=0 and n<= i:
    for digito in binario[::-1]:
        digito = int(digito)
        x = digito * (2**n)
        i -= 1
        n = n + 1
        decimal = decimal + x
else:
    print(f'o valor em decimal é {decimal}')