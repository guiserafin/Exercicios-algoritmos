def soma_valores():
    """
    retorna a soma dos valores digitados pelo usuário até que ele retorne uma string vazia
    """
    numero = input("Informe um número: ")
    if numero =="":
        return 0
    return float(numero) + soma_valores()


print(f"A soma total dos valrores informados é: {soma_valores()}")





    