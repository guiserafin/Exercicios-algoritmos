"""Área de um terreno. Crie um programa Python que leia as dimensões de um terreno em
metros (largura e profundidade), e exiba o resultado em hectares."""

x = float(input("Informe o comprimento do terreno em metros: "))
y = float(input("Informe a largura do terreno em metros: "))

area = x * y

areaHectares = area / 10000

print("A área do terreno é de "+str(areaHectares)+" hectares")