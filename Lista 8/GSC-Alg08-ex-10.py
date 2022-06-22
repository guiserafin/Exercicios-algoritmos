
def DescomprimeLista(lista):
    lista_descomprimida = []
    x = len(lista)
    if x == 2:
        for elemento in lista:
            if elemento.isdecimal():
                p = 0
                while p < int(elemento):
                    lista_descomprimida.append(lista[0])
                    p+=1
    else:
            lista_descomprimida = DescomprimeLista(lista[0:2]) + DescomprimeLista(lista[2:x])
    
    return lista_descomprimida

#print(DescomprimeLista(['A','5','B','3','C','2']))

def main():
    print("Monte a lista comprimida:\n")
    lista = []

    a = 0
    b = 0
    while a != "" and b != "":
        a = str(input("Insira um texto (Enter para parar): "))
        lista.append(a)
        b = str(input("Insira a quantidade de vezes que o texto se repete(enter para parar): "))
        lista.append(b)

    del(lista[len(lista)-2:])
    
    print(f"Sua lista comprimida: {lista}")
    print(f"Sua lista descomprimida: {DescomprimeLista(lista)}")

if __name__ == "__main__":   
    main()