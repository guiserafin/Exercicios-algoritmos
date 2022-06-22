ja_calculados = {1:0, 2:1}
def fibonacci_v2(n):
    if n in ja_calculados:
        return ja_calculados[n]
    resultado = fibonacci_v2(n-1) + fibonacci_v2(n-2)
    ja_calculados[n] = resultado
    return resultado

def main():
    numero = int(input("Informe a posição da sequência de Fibonacci que você deseja saber o valor: "))
    print(f"A posição {numero} corresponde ao número {fibonacci_v2(numero)} na sequência de Fibonacci")

if __name__ == '__main__':
    main()

"""0 1 1 2 3 5 8 13 21 34 55
   1 2 3 4 5 6 7 8  9  10 11"""
