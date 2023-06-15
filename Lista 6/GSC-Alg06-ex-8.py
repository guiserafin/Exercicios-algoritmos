def main():

    frase = input('Insira uma frase: ')
    somentePalavras(frase)


def somentePalavras(frase):

    caracteresEspeciais = ['.', '?', '!', ',' , ';']

    novaFrase = frase

    for caractere in caracteresEspeciais:
        novaFrase = novaFrase.replace(caractere, '')
        novaFrase = novaFrase

    listaPalavras = novaFrase.split(' ')

    print(listaPalavras)

main()