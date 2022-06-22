import random

def gerarCartela(): #Gera a cartela de bingo

    bingo = {'B':'temp','I':'temp','N':'temp','G':'temp','O':'temp'}
    inicio = 1
    fim = 15
    for letra in bingo:
        valores = []
        while len(valores)<5:
            valores.append(random.randint(inicio, fim))
        bingo[letra] = valores
        valores.clear
        inicio = inicio + 15
        fim = fim + 15

    return bingo

def desenharCartela(dados):

    cartela =            "---------------------\n"
    cartela = cartela + ("| B | I | N | G | O | ")

    for pos in range(0,5):
        if (dados['B'][pos] < 10):            
            cartela = cartela + (f"\n| {dados['B'][pos]} " + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
        else:             
            cartela = cartela + (f"\n| {dados['B'][pos]}" + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
    
    cartela = cartela + "\n---------------------"
    return cartela

def verificarCartela(valores,bingo):
    """valores = numeros sorteados
    bingo = cartela a ser verificada"""

    items = set()
    valores = set(valores)
    for pos in range(0,5):  #Verificar linhas
        for letra in bingo:
            items.add(bingo[letra][pos])
        if items.issubset(valores):
            return True
        items.clear()
    
    items.clear()

    for letra in bingo:   #Verificas as colunas
        for pos in range(0,5):
            items.add(bingo[letra][pos])
        if items.issubset(valores):
            return True
        items.clear()
    
    items.clear()
    inicio = -1 
    for letra in bingo:  #Verificar as diagonais
        inicio +=1
        items.add(bingo[letra][inicio])

    if items.issubset(valores):
        return True
    
    items.clear()
    inicio = -1
    for letra in "OGNIB":
        inicio = inicio + 1
        items.add(bingo[letra][inicio])
    if items.issubset(valores):
        return True
    
    return False

def main():
    #Aqui serão testadas todas as possibilidades de vitória no bingo (as tabelas estarão tortas pois o número de teste é menor que 10)

    #Cartela diagonal
    bingo = {'B': [15, 3, 4, 11, 0], 'I': [16, 9, 20, 0, 30], 'N': [43, 8, 0, 42, 39], 'G': [47, 0, 49, 2, 49], 'O': [0, 73, 64, 66, 6]}
    print(bingo)
    print(desenharCartela(bingo))
    if (verificarCartela({0}, bingo)):
        print("Cartela vencedora")
    else:
        print("Cartela perdedora")

    #Cartela diagonal
    bingo = {'B': [0, 3, 4, 11, 75], 'I': [16, 0, 20, 0, 30], 'N': [43, 8, 0, 42, 39], 'G': [47, 16, 49, 0, 49], 'O': [8, 73, 64, 66, 0]}
    print(bingo)
    print(desenharCartela(bingo))
    if (verificarCartela({0}, bingo)):
        print("Cartela vencedora")
    else:
        print("Cartela perdedora")

    #Cartela horizontal
    bingo = {'B': [0, 3, 1, 11, 65], 'I': [0, 9, 2, 59, 30], 'N': [0, 8,3, 42, 39], 'G': [0, 26, 4, 2, 49], 'O': [0, 73, 5, 66, 6]}
    print(bingo)
    print(desenharCartela(bingo))
    if (verificarCartela({5,2,3,1,4}, bingo)):
        print("Cartela vencedora")
    else:
        print("Cartela perdedora")

    #Cartela vertical
    bingo = {'B': [0, 0, 0, 0, 0], 'I': [16, 9, 20, 65, 30], 'N': [43, 8, 12, 42, 39], 'G': [47, 58, 49, 2, 49], 'O': [6, 73, 64, 66, 6]}
    print(bingo)
    print(desenharCartela(bingo))
    if (verificarCartela({0}, bingo)):
        print("Cartela vencedora")
    else:
        print("Cartela perdedora")

    #Cartela aleatória
    bingo = gerarCartela()
    print(bingo)
    print(desenharCartela(bingo))
    if (verificarCartela({0}, bingo)):
        print("Cartela vencedora")
    else:
        print("Cartela perdedora")

if __name__=="__main__":
    main()