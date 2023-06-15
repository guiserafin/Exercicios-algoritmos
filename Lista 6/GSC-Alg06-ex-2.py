def bubbleSortInverso(lista):
    for numero in range(len(lista) -1 , 0, -1):
        for i in range(numero):
            if lista[i] < lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    
    return lista

def main():
    lista = []
    while True:
        numero = int(input("Insira um número na lista (0 para parar): "))
        if numero != 0:
            lista.append(numero)
        else:
            break

    newLista = bubbleSortInverso(lista)
    print(f"A lista em ordem decrescente fica: {newLista}")


main()