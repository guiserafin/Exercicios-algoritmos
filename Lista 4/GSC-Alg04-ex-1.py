numeros = []
while True:

    x = int(input('Insira um número na soma (0 para parar)'))

    if len(numeros) == 0 and x == 0:

        print('Insira pelo menos um numero diferente de 0')

    elif  x==0 and len(numeros) > 0:

        break
    
    else:
        numeros.append(x)

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(f'A média dos números é: {media}')