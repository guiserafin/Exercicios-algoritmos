def DecBinRec(q):
    """
    retorna o binário de um número decimal inteiro 'q' usando recursividade
    """
    result = ""
    if q == 0 or q == 1:
        result += str(q)
    else:
        result = result + str(q%2)
        result = result + DecBinRec(q//2)
   
    return result

def main():
    numero = int(input("Insira um número: "))

    print(f"{numero} em binário é: {DecBinRec(numero)[::-1]}")

if __name__ == "__main__":
    main()