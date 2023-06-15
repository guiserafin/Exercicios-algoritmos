lista_negativos = []
lista_zeros     = []
lista_positivos = []
lista_geral     = []
numero          = 0

while True:

    numero = input("Insira um número na lista (Enter para parar): ")

    if (numero == ""):

        lista_geral.append(lista_negativos)
        lista_geral.append(lista_zeros)
        lista_geral.append(lista_positivos)
        break

    numero = int(numero)

    if numero < 0:
        lista_negativos.append(numero)
    elif numero == 0:
        lista_zeros.append(numero)
    else:
        lista_positivos.append(numero)

def retornaNumero(lista):

    for elemento in lista:
        
        if type(elemento) != list:
            print(elemento)
            
        else:
            retornaNumero(elemento)

retornaNumero(lista_geral)