def ComprimeLista(lista):
    lista_comprimida = []
    x = len(lista)
    if len(set(lista)) == 1:
        for elemento in lista:
            contagem = lista.count(elemento)
        lista_comprimida.append(contagem)
        while contagem > 1:
            contagem -=1
        else:
            lista_comprimida.append(elemento)
    else:
        ocorrencia = lista.count(lista[0])
        lista_comprimida = ComprimeLista(lista[0:ocorrencia]) + ComprimeLista(lista[ocorrencia:])
    
    return lista_comprimida

def main():
    x = input("Insira a lista decodificada (SEM VÍRGULAS): ")
    x = list(x)

    print(f"Aqui está a lista codificada: {ComprimeLista(x)}")

if __name__ == "__main__":
    main()
