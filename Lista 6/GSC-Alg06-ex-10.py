def formataLista(lista):

    listaString = ', '.join(lista)

    retorno = listaString[::-1].replace(',', 'e ', 1)

    return retorno[::-1]


def main():

    listaCompras = []
    while True:
        
        item = input('Insira um item na lista de compras(Enter p/ parar): ')
        
        if item == '':

            print('Sua lista de compras comtem: ',formataLista(listaCompras))
            break
        else:
            listaCompras.append(item)

main()