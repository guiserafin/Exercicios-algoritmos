def triangulo(c1,c2,c3):
    if c1 < c2+c3:
        return 'válido'
    elif c2 < c1+c3:
        return 'válido'
    elif c3 < c1+c2:
        return 'válido'
    else:
        return "inválido"

c1 = input(("Insira o valor do primeiro lado: "))
c2 = input(("Insira o valor do segundo lado: "))
c3 = input(("Insira o valor do terceiro lado: "))

print(f'Triangulo {triangulo(c1,c2,c3)}')
