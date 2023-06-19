def diferencaSimetrica(conj1, conj2):

    difSim = []

    for item in conj1:
        if item not in conj2:
            difSim.append(item)
            
    for item in conj2:
        if item not in conj1:
            difSim.append(item)

    return set(difSim)


def main():
    
    listaConjunto1 = []
    listaConjunto2 = []
    while True:
        num = input('Insira um numero no primeiro conjunto (enter para)')
        if num == '':
            break
        else:
            listaConjunto1.append(num)

    while True:
        num = input('Insira um numero no segundo conjunto (enter para)')
        if num == '':
            break
        else:
            listaConjunto2.append(num)
    
    conjunto1 = set(listaConjunto1)
    conjunto2 = set(listaConjunto2)

    print('Primeiro conjunto: ', conjunto1)
    print('Segundo conjunto: ', conjunto2)
    print('Diferença simétrica entre eles: ', diferencaSimetrica(conjunto1, conjunto2))

main()