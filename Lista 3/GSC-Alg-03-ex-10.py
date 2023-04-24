posicao = input('Insira a posição da casa do tabuleiro (de a1 até h8): ')

posicaoHorizontal = posicao[0] #letra
posicaoVertical   = int(posicao[1]) #numero

if (posicaoVertical > 8):

    exit('Casa inválida') 

letrasParaNumeros = {'a':1, 'b':2, 'c':3, 'd':4,
                     'e':5, 'f':6, 'g':7, 'h':8 }

#par com par ou impar com impar = preto

if (letrasParaNumeros[posicaoHorizontal] % 2 == 0 and posicaoVertical % 2 == 0):
    
    print('É uma casa preta')

elif (letrasParaNumeros[posicaoHorizontal] != 0 and posicaoVertical % 2 != 0):

    print('É uma casa preta')

elif (letrasParaNumeros[posicaoHorizontal] % 2 == 0 and posicaoVertical % 2 != 0):

    print('É uma casa branca')

elif (letrasParaNumeros[posicaoHorizontal] != 0 and posicaoVertical % 2 == 0):

    print('É uma casa branca')

else:

    print('Casa inválida')

   
