def countRange(lista, minimo, maximo):
#Função que conta quantos numeros estao entre o intervalo minimo-maximo (incluindo-os) dentro de uma lista

    total = 0
    for i in range(minimo, maximo+1):
        total += lista.count(i)

    
    return total


def main():

    #Exemplo de uso 
    lista = [1,2,3,4,5,6,7,8,9,10]

    print(countRange(lista, 3, 8))


main()