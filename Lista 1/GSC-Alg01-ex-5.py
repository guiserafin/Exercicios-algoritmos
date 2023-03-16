"""Retorno de recicláveis. Alguns estabelecimentos retornam créditos em troca de reciclagem
de recipientes. Em um estabelecimento em particular, vasilhames de um litro ou menos geram
crédito de 10 centavos e vasilhames de mais de um litro geram créditos de 25 centavos.
Escreva um programa que leia do teclado a quantidade destes dois tipos de vasilhames a
serem reciclados. A seguir o programa deve calcular e exibir o valor total dos créditos
referentes ao retorno dos vasilhames. Pesquise sobre como formatar a saída para que a
resposta seja exibida com sinal de reais R$ e exatamente duas casas decimais."""

x = int(input("Informe a quantidade de vasilhames de 1 litro ou menos: "))
y = int(input("Informe a quantidade de vasilhames de 1 litro ou mais: "))

credito = x*0.10 + y*0.25

print("O seu crédito é de R$ %.2f"%credito)
