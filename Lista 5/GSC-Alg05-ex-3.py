"""Calculadora de envio e-commerce. Uma loja online fornece envio de seus itens pelo preço
de R$ 10,95 para o primeiro item e R$ 2,95 para cada um dos demais itens. Escreva uma
função que receba a quantidade de ítens de um pedido e retorne o valor total do envio de
acordo com essas regras. Inclua um programa principal que leia do usuário o número de itens
adquiridos e mostre o custo do envio."""

def calculadora(quantidade): #recebe como parametro a quantidade de produtos comprados
    #calculo do preço do envio de acordo com a quantidade de produtos
    if quantidade == 1:
        preco = 10.95
    elif quantidade >= 2:
        preco = 10.95 + (2.95*(quantidade - 1))
    else:
        preco = 0
    
    return preco

quantidade = int(input("Insira a quantidade de produtos comprados: "))

print(f"O preço de envio é de R${calculadora(quantidade)}")

