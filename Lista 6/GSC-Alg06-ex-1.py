lista = []
while True:
    numero = int(input("Insira um número na lista (0 para parar): "))
    if numero != 0:
        lista.append(numero)
    else:
        break
    lista.sort()
    lista_decrescente = lista[::-1]
print(f"A lista em ordem crescente fica: {lista_decrescente}")



