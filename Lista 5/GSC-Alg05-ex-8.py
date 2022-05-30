def corretor(texto):
    
    texto = texto.lower()
    texto = texto.strip()
    saida = ""
    elevarProximo = False

    for i in range(0,len(texto)):
        try:
            if (texto[i-1] == "." or "!" or "?" or i == 0):
                saida += texto[i].upper()
                if texto[i] == " ":
                    elevarProximo = True
            else:
                if(elevarProximo):
                    saida += texto[i].upper()
                    elevarProximo = False
                else:
                    saida += texto[i]
        except IndexError:
            saida += texto[i]
    return saida

def main():
    texto = input("Escreva um texto: ")
    print ("\n")
    print("Texto formatado: ", corretor(texto))

if __name__ == "__main__":
    main()