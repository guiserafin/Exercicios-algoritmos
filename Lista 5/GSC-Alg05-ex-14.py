def data_magica(dia,mes,ano):
    

    ano = str(ano)
    decada = ano[-2] + ano[-1]

    if dia*mes == int(decada):
        return True
    else:
        return False
    
def VerDiaEMes(ano,mes):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    else:
        if ano % 4 == 0 and mes == 2:
            return 29
        if (mes == 2):
            return 28
        return 30

def main():
    for ano in range(1900, 2000):
        for mes in range(1,13):
            for dia in range(1, VerDiaEMes(ano, mes) + 1):
                if data_magica(dia,mes,ano):
                    print("%d/%d/%d" %(dia,mes,ano))

if __name__ == '__main__':
    main()