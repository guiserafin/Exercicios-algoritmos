import time

def Converter_Para_Base(numero,base):
    """
    converte um numero inteiro positivo para outro na base escolhida entre 2 e 16
    retorna a string convertida
    numero = int
    base = int
    """
    saida = ""

    while True:
        resto = numero%base
        numero = numero//base
        
        if resto == 10:
            saida = "A" + saida
        elif resto == 11:
            saida = "B" + saida
        elif resto == 12:
            saida = "C" + saida
        elif resto == 13:
            saida = "D" + saida
        elif resto == 14:
            saida = "E" + saida
        elif resto == 15:
            saida = "F" + saida
        else:
            saida = str(resto) + saida
        
        if numero < base:
            if (numero == 10):
                saida = "A" + saida
            elif (numero == 11):
                saida = "B" + saida
            elif (numero == 12):
                saida = "C" + saida
            elif (numero == 13):
                saida = "D" + saida
            elif (numero == 14):
                saida = "E" + saida
            elif (numero == 15):
                saida = "F" + saida
            else:
                saida = str(numero) + saida
            break
    return saida

def Converter_Para_Decimal(numero, base):
    """Converte qualquer numero em qualquer base para um número inteiro na base 10 e retorna o inteiro convertido
    numero = string
    base = int
    """
    numero = numero.upper()
    tamanho = len(numero)
    total = 0

    i = 0
    while i < tamanho:
        if numero[i] == "A":
            algarismo = 10
        elif numero[i] == "B":
            algarismo = 11
        elif numero[i] == "C":
            algarismo = 12
        elif numero[i] == "D":
            algarismo = 13
        elif numero[i] == "E":
            algarismo = 14
        elif numero[i] == "F":
            algarismo = 15
        else:
            algarismo = int(numero[i])
        
        total = total + algarismo * (base**(tamanho - i - 1))
        i += 1

    return total

def mensagem_erro():
    """Informa uma mensagem de erro para o usuário e limpa a tela"""
    print("Erro - O valor informado não é válido")
    time.sleep(3.0)
    print("\n"*130)

def ColetarInt(texto):
    """Coleta qualquer numero inteiro com tratamento de exceção
    texto = enunciado da coleta
    """
    while True:
        try:
            numero = int(input(texto))
            break
        except ValueError:
            mensagem_erro()
    return numero

def main():
    while True:
        base = input("Selecione a base para conversão (2 a 16):")

        if base == "":
            continue

        try:
            base = int(base)
            if base < 2 or base > 16:
                mensagem_erro()
                continue
        except ValueError:
            mensagem_erro()
            continue
        print("\n"*130)
        break

    while True:
        print("1 - Converter de base 10 para base %d" %base)
        print("2 - Converter de base %d para base 10" %base)
        print()
        escolha = int(input("Escolha uma opção"))

        if escolha == "":
            mensagem_erro()
            continue

        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > 2:
                mensagem_erro()
                continue
        except ValueError:
            mensagem_erro()
            continue
        print("\n"*130)
        break
        
    if escolha == 1:
        numero = ColetarInt("Informe o número a ser convertido para a base %d" %base)
        print("\n"*130)
        print("Número na base %d: %s" %(base, Converter_Para_Base(numero,base)))
    else:
        while True:
            numero = input("Informe um número na base %d" %base)
            if numero == "":
                mensagem_erro()
                continue
            numero = numero.upper()
            valido = True
            vect = "ABCDEF"
            for letra in numero:
                try:
                    int(letra)
                except:
                    if base > 10:
                        casas = base - 10
                    for posicao in range(casas):
                        if letra == vect[posicao]:
                            valido = True
                            break
                        else:
                            valido = False
            if valido:
                break
            else:
                mensagem_erro()
        print("Numero em decimal: ", Converter_Para_Decimal(numero,base))

if __name__ == "__main__":
    main()
    