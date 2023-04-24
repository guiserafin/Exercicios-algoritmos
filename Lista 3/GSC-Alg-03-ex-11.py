from math import sqrt

print('Insira os seguintes valores da equação quadrática de acordo com a fórmula ax²+bx+c.')
a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
c = int(input('Insira o valor de c: '))

discriminante = b**2 - 4*a*c

if (discriminante < 0):

    print('A equação não possui raizes reais.')

else:

    raiz1 = (-b + sqrt(discriminante))/ (2 * a)
    raiz2 = (-b - sqrt(discriminante))/ (2 * a)

    print('As raizes da equação são: ' + str(raiz1) + ' e ' + str(raiz2))