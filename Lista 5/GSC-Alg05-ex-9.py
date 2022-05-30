def isInteger(texto):
    texto = texto.strip()
    if texto == "" or "+" or "-":
        return False
    else:
        return True

def main():
    texto = input("Escreva um texto: ")
    if isInteger == False:
        print("O texto não representa um inteiro (False)")
    else:
        print("O texto representa um inteiro (True)")

main()