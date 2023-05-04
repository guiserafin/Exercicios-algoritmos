"""Palíndromo. Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica
à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando
laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um
palíndromo. Seu programa deve exibir uma mensagem informando o resultado."""

while True:

    palavra = input("Escreva uma palavra (Enter para sair): ")
    if palavra == "":
        break

    palavra = palavra.lower()

    if (palavra == palavra[::-1]) :

        print(f"A palavra {palavra} é um palíndromo")

    else :
        print(f'A palavra {palavra} NÃO é um palíndromo')


print("Fim")
