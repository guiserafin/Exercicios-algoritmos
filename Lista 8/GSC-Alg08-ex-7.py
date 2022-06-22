def DecBinIterativo(q):
    """
    Converte um número na base decimal (q) em seu correspondente em binário
    q = int
    """
    result = ""

    while q > 0:
        r = q%2
        result = str(r) + result
        q = q//2
    
    return result

def main():
    q = int(input("Informe um número inteiro: "))

    print(f'{q} em binário é {DecBinIterativo(q)}')

if __name__ == "__main__":
    main()