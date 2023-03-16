"""Bugigangas e quinquilharias. Uma loja online oferece aos seus clientes dois tipos de
produto: bugigangas e quinquilharias. Cada bugiganga pesa 75 gramas e cada quinquilharia
pesa 112 gramas. Faça um programa Python que leia a quantidade de bugigangas e a
quantidade de quinquilharias de um pedido do usuário. A seguir, seu programa deve calcular e
exibir o peso total do pedido."""

bugigangas = int(input("Informe o número de bugigangas adquiridas: "))
quinquilharias = int(input("Informe o número de quinquilharias adquiridas: "))

peso = str(bugigangas*75 + quinquilharias*112)

print("O peso total da compra é de: "+peso+" gramas")
