"""Juros compostos. Faça de conta que você acabou de abrir uma conta de investimento que
rende 12% de juros ao ano. Os juros que você ganha são pagos ao final do ano. Escreva um
programa que começa lendo do usuário o valor inicial depositado na conta. Em seguida, o
programa deve computar e exibir o saldo da conta de investimento após 1, 2 e 3 anos. Exiba
cada valor com exatamente 2 casas decimais."""

valorInicial = int(input("Insira o investimento incial: "))

juroAno1 = (valorInicial) * 1.12**1
juroAno2 = (valorInicial) * 1.12**2
juroAno3 = (valorInicial) * 1.12**3

print("O valor após um ano será de R$ %.2f" %juroAno1)
print("O valor após dois será de R$ %.2f" %juroAno2)
print("O valor após três anos será de R$ %.2f" %juroAno3)
