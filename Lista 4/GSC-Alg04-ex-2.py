#preço dos produtos sem desconto
from math import prod


a = 4.95 
b = 9.95
c = 14.95
d = 19.95
e = 24.95

listaProdutos = [a,b,c,d,e]

print("Lista dos produtos SEM desconto:")
for produto in listaProdutos:
    print(produto)

i = 0
print("Lista dos produtos COM desconto:")
while i < 5:
    listaDesconto = listaProdutos[i] * 0.6
    print("%.2f" %listaDesconto)
    i += 1