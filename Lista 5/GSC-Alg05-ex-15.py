def hex2int(numero_hexadecimal):

    if int(numero_hexadecimal) < 10:
        print(f"{numero_hexadecimal} para decimal é {numero_hexadecimal}")
    elif numero_hexadecimal == "A":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 10')
    elif numero_hexadecimal == "B":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 11')
    elif numero_hexadecimal == "C":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 12')
    elif numero_hexadecimal == "D":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 13')
    elif numero_hexadecimal == "E":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 14')
    elif numero_hexadecimal == "F":
        print(f'{numero_hexadecimal} em hexadecimal para decimal é 15')
    else:
        print("Por favor, escolha um valor de 0 a F")
def int2hex(numero_int):
    if numero_int < 10:
        print(f"{numero_int} para decimal é {numero_int}")
    elif numero_int == 10:
        print(f"{numero_int} em hexadecimal é 'A'")
    elif numero_int == 11:
        print(f"{numero_int} em hexadecimal é 'B'")
    elif numero_int == 12:
        print(f"{numero_int} em hexadecimal é 'C'")
    elif numero_int == 13:
        print(f"{numero_int} em hexadecimal é 'D'")
    elif numero_int == 14:
        print(f"{numero_int} em hexadecimal é 'E'")
    elif numero_int == 15:
        print(f"{numero_int} em hexadecimal é 'F'")
    else:
        print("Por favor, escolha um valor de 0 a 15")

def main():
    numero_hexadecimal = input("Selecione um número em hexadecimal de 0 a F para converter para decimal: ")
    hex2int(numero_hexadecimal)
    numero_int = int(input("Selecione um número decimal de 0 a 15 para converter para hexadecimal: "))
    int2hex(numero_int)

if __name__ == "__main__":
    main()


