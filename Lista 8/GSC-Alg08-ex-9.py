import cmath

def RaizQuadradaRec(n,estimativa):
    """
    n é o número para o qual a raiz quadrada está sendo calculada
    estimativa é a estimativa atual para a raiz quadrada // valor padrão de 1
    """
    #Caso base:
    if abs(estimativa**2 - n) <= 10**(-12):
        return estimativa
    else:
        parametro2 = (estimativa + (n/estimativa))/2
        return RaizQuadradaRec(n,parametro2)
    
def main():

    n = int(input("Insira o número cujo você deseja saber a raiz quadrada: "))

    print(f"A raíz quadrada de {n} é: {RaizQuadradaRec(n,1)}")
if __name__ == "__main__":
    main()
