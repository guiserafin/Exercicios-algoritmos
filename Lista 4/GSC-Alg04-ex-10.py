"""Palíndromo. Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica
à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando
laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um
palíndromo. Seu programa deve exibir uma mensagem informando o resultado."""
palavra = 0
while palavra != "":
    palavra = input("Escreva uma palavra (Enter para sair): ")
    palavra = palavra.lower()
    if palavra == palavra[::-1] and palavra != "":
        print(f"A palavra {palavra} é um palíndromo")
    elif palavra != palavra[::-1] and palavra != "":
        print(f'A palavra {palavra} NÃO é um palíndromo')
else:
    print("Fim")
