def precedencia(operador):
    
    if operador == "+" or operador == "-":
        return 1
    elif operador == "*" or operador == '/':
        return 2
    elif operador == "^":
        return 3
    else:
        return (-1)

def main():
    operador = input("Insira um operador matemático (+, -, *, / ou ^): ")

    if precedencia(operador) == -1:
        print("Erro - Insira um operador válido")
    else:
        print(f"A precedência do operador é: {precedencia(operador)}")

main()
