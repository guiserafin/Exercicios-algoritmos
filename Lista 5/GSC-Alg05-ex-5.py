"""Números ordinais. Palavras como primeiro, segundo e terceiro são chamadas de números
ordinais. Neste exercício, você deve escrever uma função que recebe um inteiro como seu
único parâmetro e retorna uma string contendo o número ordinal em português como seu
único resultado. Sua função deve lidar com números inteiros entre 1 e 12 (inclusive). Ela deve
retornar uma string vazia se um valor fora desse intervalo for fornecido como um parâmetro.
Inclua um programa principal que demonstra sua função exibindo cada inteiro de 1 a 12 e seu
respectivo número ordinal."""

def ordinal(n):
    if n == 1:
        return "primeiro"
    elif n == 2:
        return "segundo"
    elif n == 3:
        return "terceiro"
    elif n == 4:
        return "quarto"
    elif n == 5:
        return "quinto"
    elif n == 6:
        return 'sexto'
    elif n == 7:
        return 'sétimo'
    elif n == 8:
        return 'oitavo'
    elif n == 9:
        return 'nono'
    elif n == 10:
        return 'décimo'
    elif n == 11:
        return 'décimo primeiro'
    elif n == 12:
        return 'décimo segundo'

n = int(input("Escolha um número de 1 a 12: "))
if n > 0 and n<12:
    print(f'O ordinal desse número é {ordinal(n)}')
else:
    print('')
