palavra = ""
lista = []
def remove_repeticoes(lista):
    while True:
        palavra = input("Escreva uma palavra (Enter para parar): ")
        if palavra != "":
            if palavra not in lista:
                lista.append(palavra)
        else:
            break
    print(lista)

remove_repeticoes(lista)