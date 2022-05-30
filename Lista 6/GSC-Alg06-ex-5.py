lista_negativos = []
lista_zeros = []
lista_positivos = []
numero = 0
while True:
    numero = input("Insira um número na lista (Enter para parar): ")
    if numero == "":
        break

    numero = int(numero)
    if numero < 0:
        lista_negativos.append(numero)
    elif numero == 0:
        lista_zeros.append(numero)
    else:
        lista_positivos.append(numero)

print(f"Os números negativos da lista são: {lista_negativos}")
print(f"Os números zeros da lista são: {lista_zeros}")
print(f"Os números positivos da lista são: {lista_positivos}")

