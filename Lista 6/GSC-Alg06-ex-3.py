from sort import bubbleSort

def remove_extremos(lista,numero):

    if len(lista) < 4:

        print("Erro - Insira pelo menos 4 valores.")

    else:
        lista = sorted(lista)
        lista.remove(lista[0])
        lista.remove(lista[1])
        lista.remove(lista[-1])
        lista.remove(lista[-2])

        print(f"A lista sem os extremos: {lista}")

def main():
    lista = []

    while True:
        numero = int(input("Insira um número na lista (0 p/ parar): "))
        if numero != 0:
            lista.append(numero)
        else:
            break

    remove_extremos(lista, 2)

main()