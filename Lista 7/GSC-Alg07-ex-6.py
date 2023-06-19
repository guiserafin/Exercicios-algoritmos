import string
import unicodedata

def tratarString(texto):
    # Remove espaços
    texto = texto.replace(" ", "")

    # Remove pontuação
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    # Remove acentuação
    texto = ''.join(
        (c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
    )

    #deixa em letras maiúsculas
    texto = texto.upper()

    return texto

def verificaAnagrama(frase1, frase2):

    str1 = tratarString(frase1)
    str2 = tratarString(frase2)

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
    frase1 = input("Insira uma frase: ")
    frase2 = input("Insira outra frase: ")

    if verificaAnagrama(frase1, frase2):
        print("São anagramas")
    else:
        print("Não são anagramas") 

main()

