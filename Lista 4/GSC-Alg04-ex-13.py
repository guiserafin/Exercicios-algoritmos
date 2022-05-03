n = int(input("Digite um número inteiro maior ou igual a 2: "))
fator = 2
while fator <= n:
    if (n%fator) == 0:
        n = n/fator
        print(fator)
    else:
        fator += 1