def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)
    
def main():
    n = int(input('Digite o número que você deseja saber o valor fatorial: '))
    print(f'{n}! = {fatorial(n)}')

if __name__ == "__main__":
    main()
    