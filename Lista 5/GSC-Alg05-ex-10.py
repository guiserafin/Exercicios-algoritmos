def primo(n):
    """Define se um número é primo ou não, se for primo retorna True 
    e se não for retorna False
    n = número"""

    for i in range(2,9):
        if n == 2:
            return True
        elif n%i != 0:
            return True
        elif n%i ==0:
            return False

def main():
    n = int(input("Insira um número: "))
    if primo(n) == True:
        print("O número é primo")
    else:
        print("O número não é primo")

main()
