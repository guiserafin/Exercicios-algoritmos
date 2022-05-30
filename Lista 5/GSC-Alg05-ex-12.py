def verificar_senha(senha):
    
    maiuscula = 0
    minuscula = 0
    numero = 0

    for i in senha:
        if i.isupper():
            maiuscula = maiuscula + 1
        if i.islower():
            minuscula = minuscula + 1
        if str.isnumeric(i):
            numero = numero + 1

    if minuscula < 1 or maiuscula < 1 or numero < 1 or len(senha) < 8:
        return False
    else:
        return True

def main():
    senha = input("Defina uma senha com letras maiusculas, minusculas e números e com pelo menos 8 caracteres (espaços serão ignorados): ")
    senha = senha.strip()
    senha = senha.replace(" ", "")

    if verificar_senha(senha) == False:
        print("Senha inválida")
    else:
        print("Senha válida")

if __name__ == "__main__":
    main()
