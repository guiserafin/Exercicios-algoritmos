def primo(n):
    """Define se um número é primo ou não, se for primo retorna True 
    e se não for retorna False
    n = número"""

    divisores = []

    for i in range(1, n+1):
        if n % i == 0:
            divisores.append(i)
    
    if (len(divisores) > 2):
        return False
    else:
        return True

def main():
    n = int(input("Insira um número: "))
    if primo(n):
        print("O número é primo")
    else:
        print("O número não é primo")

main()
