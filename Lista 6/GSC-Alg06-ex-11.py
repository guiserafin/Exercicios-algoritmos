from random import randint
from sort import bubbleSort

def megaSena():

    numerosSorteados = []

    while len(numerosSorteados) < 6:

        numero = randint(1, 60)

        if numero not in numerosSorteados:
            numerosSorteados.append(numero)
        
    
    print('Os numeros sorteados são: ', bubbleSort(numerosSorteados))


megaSena()