"""Soma dos dígitos de um inteiro. Desenvolva um programa que obtenha do usuário um
número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1)."""

numero = int(input("Digite um número de 4 dígitos: "))
while len(str(numero)) != 4:
    numero = int(input("Digite um número de 4 dígitos: "))

soma = 0
for digito in str(numero) :
    soma += int(digito)

print("A soma dos números é", soma)


