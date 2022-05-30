def remove_extremos(lista,numero):
    while True:
        numero = int(input("Insira um número na lista: "))
        n = 0
        if numero != 0:
            n += 1
            lista.append(numero)
            lista.sort()
        else:
            if len(lista) < 4:
                print("Erro - Insira pelo menos 4 valores.")
                lista = []
            else:
                lista.remove(lista[0])
                lista.remove(lista[n-1])
                print(f"A lista sem os extremos: {lista}")
                break

def main():
    lista = []
    numero = 1
    remove_extremos(lista, numero)

if __name__ == "__main__":
    main()
