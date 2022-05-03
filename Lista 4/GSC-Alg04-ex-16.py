"""Cara ou coroa. Qual é o menor número de vezes que você precisa sortear uma moeda para
ter três resultados consecutivos iguais de cara ou de coroa? Qual é o número máximo de
sorteios necessários? Quantos sorteios precisamos em média? Neste exercício vamos
explorar estas questões criando um programa que simula várias séries de sorteios de cara ou
coroa.
Crie um programa que utilize o gerador de números randômicos do Python para simular o
sorteio de uma moeda várias vezes. A moeda simulada deve ser justa, ou seja, deve ter a
mesma probabilidade de gerar cara e coroa. Seu programa deve continuar simulando sorteios
até que ocorra uma sequencia de 3 caras ou de 3 coroas consecutivas. Exiba A para cada vez
que ocorrer cara e O para cada vez que ocorrer coroa, com todos os resultados sendo
exibidos na mesma linha. Então exiba a quantidade de sorteios que levou para chegar a três
resultados iguais consecutivos. Quando seu programa executar, ele deve fazer esta simulação
10 vezes e, ao final, mostrar a quantidade média de sorteios necessária."""

import random
# A = cara
# O = Coroa
quantidade = 0
sorteios = 0

while quantidade <10 :
    cara = 0
    coroa = 0
    sorteioLocal = 0
    while True:
        lado = random.randint(1,2)
        if lado == 1:
            print("A", end = " ")
            cara += 1
            coroa = 0
        else:
            print("O", end = " ")
            coroa += 1 
            cara = 0
        sorteioLocal +=1
        if cara == 3 or coroa == 3:
            print(sorteioLocal, "sorteios")
            sorteios += sorteioLocal
            break
    quantidade +=1

media = sorteios/10

print(f'Na média foram necessários {media} sorteios')

