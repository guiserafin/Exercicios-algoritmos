def dias_mes(mes,ano):
    """recebe como parametro um mês e um ano e diz quantos dias há nesse mês
    mês = int entre 1 e 12
    ano = int"""

    if ano%4 == 0: #ano bissexto:
        if mes == 2:
            print("29 dias")
        elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("30 dias")
        else:
            print('31 dias')
    else: #anos não bissextos
        if mes == 2:
            print("28 dias")
        elif mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print("30 dias")
        else:
            print("31 dias")

def main():
    mes = int(input("Insira um mês de 1 a 12: "))
    ano = int(input("Insira um ano: "))
    
    while mes < 1 or mes > 12:
        print("Erro - Selecione um mês de 1 a 12")
        mes = int(input("Insira um mês de 1 a 12: "))
        ano = int(input("Insira um ano: "))

    dias_mes(mes, ano)

if __name__ == "__main__":
    main()
