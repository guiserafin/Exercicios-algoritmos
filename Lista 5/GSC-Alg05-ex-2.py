"""Tarifa do táxi. Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de
R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como
seu único parâmetro a distância percorrida em quilômetros, e retorna como seu único
resultado o valor total da corrida. Escreva um programa principal que demonstre o
funcionamento de sua função."""

fixo = 4 #valor inicial de 4 reais
valor_por_140m = 0.25
DISTANCIA_POR_TARIFA = 0.14 #distancia padrão da tarifação

def tarifa(distancia):
    total = fixo + ((distancia/DISTANCIA_POR_TARIFA) * valor_por_140m) #valor inicial somado a distância divido por 140 metros vezes 0,25 centavos
    return total

distancia = float(input("Insira a distância percorrida em kilômetros: ")) #pede a distância percorrida para o usuario

print(f"A tarifa total é de R$",tarifa(distancia))
