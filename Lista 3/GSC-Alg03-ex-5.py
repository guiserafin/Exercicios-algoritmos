mes = input('Insira o mês: ').lower()

meses30 = ['abril', 'junho', 'setembro', 'novembro']
meses31 = ['janeiro', 'março', 'marco', 'maio', 'julho', 'agosto', 'outubro', 'dezembro']

if mes == 'fevereiro':

    print('28 ou 29 dias')

elif mes in meses30:

    print('30 dias')

elif mes in meses31:

    print('31 dias')

else:

    print('Mês inválido')