def corretor(texto):
    
    texto = texto.lower()
    texto = texto.strip()
    saida = ""
    elevarProximo = False

    for i in range(0,len(texto)):

        pontuacao = ['.', '!', '?']
        
        if (texto[i-1] in pontuacao or (texto[i-2] in pontuacao and texto[i] != ' ') or i == 0):

            saida += texto[i].upper()

                
        else:
        
            saida += texto[i]


    return saida

def main():
    texto = input("Escreva um texto: ")
    print ("\n")
    print("Texto formatado: ", corretor(texto))


main()