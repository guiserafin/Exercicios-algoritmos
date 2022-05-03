"""Soma dos dígitos de um inteiro. Desenvolva um programa que obtenha do usuário um
número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário
fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1)."""

numero = int(input("Digite um número de 4 dígitos: "))
while numero > 9999 or numero < 1000:
    numero = int(input("Digite um número de 4 dígitos: "))

numero = str(numero)

numero1 = numero[0]
numero2 = numero[1]
numero3 = numero[2]
numero4 = numero[3]

numero1 = int(numero1)
numero2 = int(numero2)
numero3 = int(numero3)
numero4 = int(numero4)

soma = numero1 + numero2 + numero3 + numero4

print("A soma dos números é", soma)


