"""Centena, dezena, unidade. Dado um número de três algarismos N = CDU (onde C é o
algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um
programa Python que receba do usuário o número inteiro N, e imprima separadamente a
centena, a dezena e a unidade."""

numero = int(input("Digite um número de 3 dígitos: "))
while numero > 999 or numero < 100:
    numero = int(input("Digite um número de 3 dígitos: "))

numero = str(numero)

centena = numero[0]
dezena = numero[1]
unidade = numero[2]

print("A centena é: ", centena, "A dezena é: ", dezena, "A unidade é: ", unidade)