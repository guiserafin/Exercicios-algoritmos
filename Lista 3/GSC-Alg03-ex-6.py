l1 = input('Insira o comprimento de um lado do triangulo: ')
l2 = input('Insira o comprimento de outro lado do triangulo: ')
l3 = input('Insira o comprimento do ultimo lado do triangulo: ')

if l1 == l2 and l2 == l3:

    print('É um triângulo equilátero.')

elif l1 == l2 and l2 != l3:

    print('É um triangulo isósceles')

else :

    print('É um triângulo escaleno')