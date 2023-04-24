feriados = {'1/1'  : 'Confraternização universal',
            '21/4' : 'Tiradentes',
            '1/5'  : 'Dia do trabalho',
            '7/9'  : 'Independência do Brasil',
            '12/10': 'Nossa Senhora Aparecida',
            '2/11' : 'Finados',
            '15/11': 'Proclamação da república',
            '25/12': 'Natal'
            }

dia = int(input('Insira o dia: '))
mes = int(input('Insira o mês (numero): '))

chave = str(dia) + '/' + str(mes)

if (chave in feriados):
    
    print('Esse dia corresponde ao feriado de ' + feriados[chave])

else:

    print('Este dia não corresponde a nenhum feriado')