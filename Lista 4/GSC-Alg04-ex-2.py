#preço dos produtos sem desconto
listaProdutos = [4.95, 9.95, 14.95, 19.95, 24.95]

print("Lista dos produtos SEM desconto:")
for produto in listaProdutos:
    print(produto, end=", ")

i = 0
print()
print("Lista dos produtos COM desconto:")
while i < 5:
    listaDesconto = listaProdutos[i] * 0.6
    print("%.2f" %listaDesconto, end=", ")
    i+=1
print()