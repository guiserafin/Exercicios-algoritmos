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


def charsToMorse(frase):

    dicionarioMorse = {'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F': '..-.', 'G' : '--.', 'H' : '....', 'I' : '..',
            'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.',
            'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..', '0': '-----',
            '1' : '.----', '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..',
            '9' : '----.' 
    }

    fraseMorse = ''

    for caractere in tratarString(frase):
        fraseMorse += dicionarioMorse[caractere] + ' '

    return fraseMorse

def main():
    frase = input('Insira uma frase para vê-la em código morse: ')
    print('Sua frase em morse: ', charsToMorse(frase))

main()