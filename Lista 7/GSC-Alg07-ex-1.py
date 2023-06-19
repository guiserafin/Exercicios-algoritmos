def caracteres_unicos(palavra):
    """Define se um palavra repete caracteres ou não
    se repete = retorna False
    Se não repete = retorna True
    palavra = string
    """
    conjunto_de_letras = set()
    palavra = palavra.strip()

    for letra in palavra:
        conjunto_de_letras.add(letra)

    if len(conjunto_de_letras) == len(palavra):
        return True
    else:
        return False

def main():
    palavra = input("Insira uma palavra: ")

    if caracteres_unicos(palavra):
        print("A palavra não repete caracteres")
    else:
        print("A palavra repete caracteres")

main()
