#distância entre dois pontos = math.sqrt((y2 - y1)**2 + (x2-x1)**2)

import math
x1 = 0
y1 = 0

x2 = 0
y2 = 0

perimetro = 0
while x1 != "":
    x1 = (input("Digite a coordenada X de um ponto (Enter para sair): "))
    y1 = (input("Digite a coordenada Y de um ponto: "))

    x2 = (input("Digite a coordenada X de OUTRO ponto: "))
    y2 = (input("Digite a coordenada Y de OUTRO ponto: "))

    if x1 != "":
        dist = math.sqrt((int(y2)-int(y1))**2 + (int(x2) - int(x1))**2)
        print(f"A distância entre esses pontos é {dist}")
        perimetro = perimetro + dist
        print(f"O perímetro do polígono é {perimetro}")
else:
    print("Fim do programa")

    