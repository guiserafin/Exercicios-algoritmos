"""12. Área e volume. Escreva um programa Python que começa lendo o valor de um raio r,
fornecido pelo usuário. O programa deve continuar calculando e exibindo a área de um círculo
de raio r, e o volume de uma esfera de raio r. Utilize a constante pi do módulo math nos seus
cálculos."""
import math
r = float(input("Informe o raio: "))

volume = (4/3)*(math.pi)*r**3
area = math.pi*(r**2)


print("O volume da esfera é: %.2f unidades de volume " %volume)
print("A área do circulo é de: %.2f unidades de área" %area)

