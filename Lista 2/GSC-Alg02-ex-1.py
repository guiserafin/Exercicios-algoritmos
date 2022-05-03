"""
Unidades de tempo. Crie um programa Python que leia do usuário um valor de
intervalo de tempo expresso em número de dias, horas, minutos e segundos.
O programa deve computar eexibir a quantidade total de segundos deste
intervalo de tempo informado.

"""
dias = int(input("Insira o número de dias "))
horas = int(input("Insira o número de horas "))
minutos = int(input("Insira o número de minutos "))
segundos = int(input("Insira o número de segundos "))

total_de_segundos = 86400*dias + 3600*horas + 60*minutos + segundos

print("O total de segundos é %.2f" % total_de_segundos)


