def BuscaReversa(valor,dicionario):
    """
    Retorna as chaves do dicionario de acordo com o valor informado
    """
    lista = []
    for k,v in dicionario.items():
        if v == valor:
            lista.append(k)
    
    return lista

def main():
    dicionario = {'valor' : 1, 'valor2':2, 'valor3':2, 'valor4':2, 'valor5': 5}
    valor = 2
    lista = BuscaReversa(valor,dicionario)

    if len(lista) == 0:
        print("Nenhum valor encontrado")
    else:
        print("Valores encontrados: ", lista)

if __name__ == "__main__":
    main()

