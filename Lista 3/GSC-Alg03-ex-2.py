idadeCronologica = int(input('Insira a idade do cachorro: '))

if idadeCronologica <= 0:
    exit('Erro. Idade inválida')


if idadeCronologica <= 2:
    
    idadeCanina = idadeCronologica * 10.5

else:

    idadeCanina = ((idadeCronologica - 2) * 4 ) + 21

print('A idade canina do animal é de ' + str(idadeCanina) + ' anos')
