def main():

    listaNumeros = []

    while True:

        x = input('Insira um numero na lista(Enter p/ sair): ')

        if x == '':

            soma = 0
            for numero in listaNumeros:
                soma+=numero
            
            media = soma/len(listaNumeros)
            
            acimaMedia  = []
            abaixoMedia = []
            naMedia     = []

            for numero in listaNumeros:

                if numero > media:
                    acimaMedia.append(numero)
                elif numero < media:
                    abaixoMedia.append(numero)
                else:
                    naMedia.append(numero)

            break
        else:
            listaNumeros.append(int(x))

    print('Numeros: ', listaNumeros)
    print('Numeros acima da media: ', acimaMedia)
    print('Numeros na media: ', naMedia)
    print('Numeros abaixo da media: ', abaixoMedia)


main()