"""Centena, dezena, unidade (novamente). Dado um número de três algarismos N = CDU
(onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das
unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é,
M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123
->M=321)."""

numero = int(input("Digite um número de 3 dígitos: "))
while numero > 999 or numero < 100:
    numero = int(input("Digite um número de 3 dígitos: "))

numero = str(numero)

centena = numero[0]
dezena = numero[1]
unidade = numero[2]

print(unidade+dezena+centena)