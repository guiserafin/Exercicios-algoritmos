def main():

    listaNumeros = []
    
    while True:

        numero = input('Insira um numero na lista: ')

        if numero != '':

            listaNumeros.append(numero)

        else:

            if (isSorted(listaNumeros)):
                print(f'A lista {listaNumeros} está ordenada corretamente')
            else:
                print(f'A lista {listaNumeros} NÃO está ordenada corretamente')
            
            break

def isSorted(prLista):

    if prLista == sorted(prLista):
        return True
    
    else:
        return False

if __name__ == '__main__':
    main()