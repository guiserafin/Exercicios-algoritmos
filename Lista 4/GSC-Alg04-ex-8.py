#Basicamente fazer um programa que transforme 'abcdefghijklmnopqrstuvwxyz' 
# ######################################## em 'defghijklmnopqrstuvwxyzabc'

frase = input("Escreva uma frase: ")

for letra in frase:
    frase_unicode = ord(letra)
    print("Frase em unicode: ",frase_unicode, end = " ")
