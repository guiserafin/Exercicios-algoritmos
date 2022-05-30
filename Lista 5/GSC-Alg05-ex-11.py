import random

comprimento_senha = random.randint(7, 10)
comprimento_senha = int(comprimento_senha)

print(f"A senha contém {comprimento_senha} dígitos")

caractere_senha = ""
caractere_senha = str(caractere_senha)


def senha(comprimento_senha, caractere_senha):
    i = 0
    for i in range(0, comprimento_senha):
        caractere_senha += chr(random.randint(33, 126))       
        i +=1
    return caractere_senha

print(senha(comprimento_senha,caractere_senha))
