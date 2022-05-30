import math

def hipotenusa(x,y): #função que calcula o valor da hipotenusa
    z = math.sqrt(x**2 + y**2)
    return z



x = float(input("Insira o valor de um dos catetos: ")) #pedir para o usuário inserir os valores dos catetos
y = float(input("Insira o valor de outro cateto: ")) 

print(hipotenusa(x,y)) #imprime o valor da hipotenusa de acordo com o x e y escolhidos
