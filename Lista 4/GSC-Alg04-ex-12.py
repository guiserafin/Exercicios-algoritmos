"""Tabela de multiplicação. Neste exercício você deve criar uma tabela de multiplicação
mostrando os produtos de todos os inteiros de 1 vezes 1 até 10 vezes 10. Sua tabela deve
incluir uma linha de cabeçalho com números de 1 a 10, e também uma coluna com os
mesmos números. A saída esperada do programa deve ser semelhante ao mostrado abaixo:"""

print("\t", end =" ")
for coluna in range (1, 11):
    print(coluna, "\t", end=" ")
print()
for linha in range (1,11):
    print(linha, "\t", end =" ")
    for coluna in range (1,11):
        print(linha*coluna, "\t", end =" ")
    print()
