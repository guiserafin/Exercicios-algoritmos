def BuscaReversa(valor,dicionario):
    """
    Retorna as chaves do dicionario de acordo com o valor informado
    """
    lista = []
    for key,value in dicionario.items():
        if value == valor:
            lista.append(key)
    
    return lista

def main():

    ##demonstração de funcionamento da função
    dicionario = {'chave1' : 1, 'chave2' : 2, 'chave3' : 2, 'chave4' : 2, 'chave5' : 5}
    valor = 2
    lista = BuscaReversa(valor,dicionario)

    if len(lista) == 0:
        print("Nenhuma chave encontrado")
    else:
        print("Chaves encontradas: ", lista)


main()

