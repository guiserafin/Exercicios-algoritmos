soma = 0
n = 0
x = 1

while x != 0:
    x = int(input('Digite um número (0 para parar): '))
    if n == 0 and x == 0:
        print("Erro - Insira pelo menos um valor diferente de 0")
        break
    elif x != 0:
        soma = soma + x 
        n += 1
else:
    media = soma / n
    print(f"A média dos números inseridos é {media}")
