"""Palíndromos com múltiplas palavras. O conceito de palíndromo também pode ser aplicado
a frases, por exemplo: “A base do teto desaba”. Faça um novo programa Python que
modifique o programa do exercício anterior para verificar se frases são palíndromos. Seu
programa vai precisar ignorar os espaços em branco das frases. Como desafio adicional,
amplie sua solução para que também ignore sinais de pontuação e trate letras maiúsculas e
minúsculas como equivalentes."""


while True:

    frase = input("Escreva uma frase (Enter para sair): ")

    if (frase == ""):
        break

    nova_frase = ''.join(filter(str.isalnum, frase)) # retira todos os espaços e caracteres especiais da frase
    nova_frase = nova_frase.lower()
    if ( nova_frase == nova_frase[::-1] ):

        print(f"A frase {frase} é um palíndromo")

    else:
        print(f'A frase {frase} NÃO é um palíndromo')


print("Fim")