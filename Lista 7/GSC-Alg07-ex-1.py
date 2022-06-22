def caracteres_unicos(palavra):
    """Define se um palavra repete caracteres ou não
    se repete = retorna False
    Se não repete = retorna True
    palavra = string
    """
    conjunto_de_letras = set()

    for letra in palavra:
        conjunto_de_letras.add(letra)

    if len(conjunto_de_letras) == len(palavra):
        return True
    else:
        return False

def main():
    palavra = input("Insira uma palavra: ")

    x = caracteres_unicos(palavra)

    if x == True:
        print("A palavra não repete caracteres")
    else:
        print("A palavra repete caracteres")

if __name__ == "__main__":
    main()
