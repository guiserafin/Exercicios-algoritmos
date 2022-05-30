"""Centralizando uma string. Escreva uma função que recebe uma string como seu primeiro
parâmetro e a largura de uma linha do terminal em caracteres como seu segundo parâmetro.
Sua função deve retornar uma nova string que consiste na string original e no número correto
de espaços iniciais para que a string original apareça centralizada dentro da largura fornecida
quando for impressa. Não adicione nenhum caractere ao final da string. Inclui um programa
principal que demonstre sua função."""
#x = 7
#print(x*"a")
import time

def central(string,espacos):
   # espacos = int(input("Insira a largura da linha"))
    #string = input("Insira a frase que deseja centralizar")
    saida = ""
    for x in range(1,espacos//2):
        saida += " "
    saida += string
    return saida

espacos = int(input("Insira a largura da linha: "))
string = input("Insira a frase que deseja centralizar: ")
print(central(string,espacos))




