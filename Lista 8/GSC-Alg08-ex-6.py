def MDC(a,b):
    """
    Determina o máximo divisor comum entre dois números
    a e b = int
    """
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        c = a%b
        return MDC(b,c)

def main():
    numero1 = int(input("Insira um número: "))
    numero2 = int(input("Insira outro número: "))
    print(f"O máximo divisor comum entre os números informados é: {MDC(numero1,numero2)}")

if __name__ == "__main__":
    main()
