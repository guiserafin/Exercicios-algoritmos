"""Área de uma sala. Escreva um programa Python que peça para o usuário os comprimentos
da largura e profundidade de uma sala. Após a leitura dos valores, seu programa deve exibir a
área da sala. A largura e a profundidade devem ser números reais. Inclua as unidades nas
mensagens de entrada e saída (metros e metros quadrados)."""

x = float(input("Informe o comprimento da sala em metros: "))

y = float(input("Informe a largura da sala em metros: "))

area = float(x) * float(y)

area = str(area)

print("A área da sala é de "+area+" metros quadrados")
