"""Data invertida. Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
em uma variável do tipo data, crie um programa Python que leia uma data no formato
DDMMAA e imprima essa data no formato AAMMDD, onde:
• a letra D corresponde a dois algarismos representando o dia;
• a letra M corresponde a dois algarismos representando o mês;
• a letra A corresponde aos dois últimos algarismos representando o ano.
Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611"""

data = input("Insira uma data no formato DDMMAA: ")

#09 10 01
data_invertida = data[4] + data[5] + data[2] + data[3] + data[0] + data[1]

print("A data invertida é: ", data_invertida)
