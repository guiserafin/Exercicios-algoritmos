"""Calculando o troco. Considere o software que controla uma máquina automática de compras.
Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando
este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario
uma quantidade de centavos como um número inteiro (portanto vamos considerar números de
0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para
compor este troco em centavos informado. O troco deve ser montado com a menor quantidade
possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos."""

centavos = int(input("Quantos centavos? (0 a 99): "))

#99 centavos -> 1 de 50 + 1 de 25 + 2 de 10 + 4 de 1
#55 centavos -> 1 de 50 + 1 de 5

moedas_de_50 = (centavos//50)
centavos = centavos - moedas_de_50*50
moedas_de_25 = (centavos//25)
centavos = centavos - moedas_de_25*25
moedas_de_10 = (centavos//10)
centavos = centavos - moedas_de_10*10
moedas_de_5 = (centavos//5)
centavos = centavos - moedas_de_5*5
moedas_de_1 = centavos

print(moedas_de_1,"moedas de 1 centavo;", moedas_de_5,"moedas de 5 centavos;", moedas_de_10,"moedas de 10 centavos;", moedas_de_25,"moedas de 25 centavos;", moedas_de_50,"moedas de 50 centavos")
