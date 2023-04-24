ano = int(input('Insira um ano para saber se o mesmo é bissexto: '))

if (ano%400 == 0 and ano%4 == 0) :
    
    print('É um ano bissexto')

elif (ano%4 == 0):
    
    print('É bissexto')

else:

    print('Não é bissexto')