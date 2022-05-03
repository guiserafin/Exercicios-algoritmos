"""6. Conta do almoço. Imagine que você foi almoçar num restaurante, e pediu uma refeição com
um suco, um prato principal e uma sobremesa. Cada um desses itens tem um preço unitário.
Ao final, o valor da conta deve ser a soma do valor dos itens consumidos, acrescida de 10%
de taxa de serviço. Faça um programa Python para receber estes dados do usuário e calcular
o valor total da conta deste tipo de refeição. Exiba a resposta com os mesmos critérios de
formatação da questão anterior (R$ e 2 casas decimais)."""


"""Supondo que o preço do suco, do prato principal e da sobremesa somados seja de R$30, já que a questão não indica nenhum preço"""

total = float(30.00)*1.1


print("O preço total a ser pago é de R$ %.2f" %total)
