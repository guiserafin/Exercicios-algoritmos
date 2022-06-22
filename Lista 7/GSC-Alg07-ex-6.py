def anagrama(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()

    string1.replace(" ","")
    string2.replace(" ","")

    letras = "abcdefghijklmnopqrstuvwxyz"
    dic1 = {}
    dic2 = {}

    for letra in string1:
        if dic1.get(letra) != None:
            dic1[letra] = dic1[letra] + 1
        elif letra in letras:
            dic1[letra] = 1
    for letra in string2:
        if dic2.get(letra) != None:
            dic2[letra] = dic2[letra] + 1
        elif letra in letras:
            dic2[letra] = 1
    
    if dic1.items() == dic2.items():
        return True
    else:
        return False

def main():
    frase1 = input("Insira uma frase: ")
    frase2 = input("Insira outra frase: ")

    if anagrama(frase1, frase2):
        print("São anagramas")
    else:
        print("Não são anagramas") 

if __name__ == "__main__":
    main()

