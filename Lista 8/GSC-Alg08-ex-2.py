def fibonacci(n):
    """
    Função que define o número na posição 'n' na sequencia de Fibonacci, onde n é a soma (n-1) + (n-2)
    n = int
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    numero = int(input("Informe a posição da sequência de Fibonacci que você deseja saber o valor: "))
    print(f"A posição {numero} corresponde ao número {fibonacci(numero)} na sequência de Fibonacci")

if __name__ == '__main__':
    main()

"""0 1 1 2 3 5 8 13 21 34 55
   1 2 3 4 5 6 7 8  9  10 11"""
