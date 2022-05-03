"""Tabela de multiplicação. Neste exercício você deve criar uma tabela de multiplicação
mostrando os produtos de todos os inteiros de 1 vezes 1 até 10 vezes 10. Sua tabela deve
incluir uma linha de cabeçalho com números de 1 a 10, e também uma coluna com os
mesmos números. A saída esperada do programa deve ser semelhante ao mostrado abaixo:"""

for i in range(1, 11):
    for j in range(1, 11):
        multiplicação = i * j
        print(multiplicação, end=" ")
        j = j + 1
    i = i + 1