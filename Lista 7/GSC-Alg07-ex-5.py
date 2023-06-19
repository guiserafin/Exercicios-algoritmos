def verificaAnagrama(str1, str2):

    # Verifica se as strings possuem o mesmo comprimento
    if len(str1) != len(str2):
        return False

    # Cria dicionários para contar a ocorrência de cada letra nas strings
    contador1 = {}
    contador2 = {}

    # Conta a ocorrência de cada letra na primeira string
    for letra in str1:
        contador1[letra] = contador1.get(letra, 0) + 1

    # Conta a ocorrência de cada letra na segunda string
    for letra in str2:
        contador2[letra] = contador2.get(letra, 0) + 1

    # Compara os dicionários de contagem de ocorrência
    return contador1 == contador2


def main():
    palavra1 = input("Insira uma palavra: ")
    palavra2 = input("Insira outra palavra: ")

    if (verificaAnagrama(palavra1, palavra2)):
        print('As palavras são anagramas')
    else:
        print('As palavras não são anagramas')

main()