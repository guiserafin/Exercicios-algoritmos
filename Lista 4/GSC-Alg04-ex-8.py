#Basicamente fazer um programa que transforme 'abcdefghijklmnopqrstuvwxyz' 
# ######################################## em 'defghijklmnopqrstuvwxyzabc'

frase = input("Escreva uma frase: ")
chave = int(input("Insira a chave da cifra: "))
resultado = ""
for letra in frase:
    letra = letra.upper()
    letraUnicodeNova = (ord(letra) - ord('A') + chave) % 26
    resultado += chr(ord('A') + letraUnicodeNova)

print(resultado)


