"""Mediana de três valores. Escreva uma função que recebe três números como parâmetros e
retorna o valor da mediana desses parâmetros como seu resultado. Inclua um programa
principal que lê três valores do usuário e exibe a mediana destes valores."""

def mediana(n1,n2,n3):
    lista = [n1,n2,n3]
    lista = sorted(lista)
    return lista[1]

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite o último número: "))

print(f'A mediana dos valores é {mediana(n1,n2,n3)}')



