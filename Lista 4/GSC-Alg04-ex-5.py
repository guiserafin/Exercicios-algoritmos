idade = 1
valor_ingresso = 0
valor_total = 0

while True:
    idade = int(input("Digite a idade da pessoa do grupo: "))
    parar = input("Deseja parar a contagem?(s ou n): ")
    if parar == 's':
        break
    if idade >0 and idade <= 2:
        valor_ingresso = 0
    elif idade >= 3 and idade <= 12:
        valor_ingresso = 14
    elif idade >= 65:
        valor_ingresso = 18
    else:
        valor_ingresso = 23
    valor_total = valor_total + valor_ingresso

print(f"O valor total do ingresso é {valor_total}")
