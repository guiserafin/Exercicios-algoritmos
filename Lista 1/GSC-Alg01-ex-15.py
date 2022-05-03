"""Escreva um programa Python que obtenha do usuário os valores de l e n, e então calcule e
exiba a área do polígono regular correspondente."""
import math
n = int(input("Insira o número de lados do polígono: "))
l = float(input("Insira o comprimento de um dos lados do polígono: "))

area = (n*(l**2))/ 4* math.tan(math.pi/n)

print("A área do polígono é de %.2f unidades de área"%area)
