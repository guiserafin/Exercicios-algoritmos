def VerificaPalindromo(string):
    """
    Função que verifica se uma palavra ou frase é um palíndromo utilizando recursividade 
    """
    c = len(string)
    if c <= 1:
        return True
    elif string[0] == string[-1] and VerificaPalindromo(string[1:-1]):
        return True
    else:
        return False

def main():
    palavra = input("Digite uma frase ou palavra: ")
    palavra = palavra.lower()
    palavra = palavra.strip()
    palavra = palavra.replace(" ","")
    x = VerificaPalindromo(palavra)
    if x:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

if __name__ == "__main__":
    main()

