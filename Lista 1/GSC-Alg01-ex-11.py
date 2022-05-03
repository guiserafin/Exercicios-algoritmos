import math
#Informar as coordenadas
t1 = int(input("Informe a latitude do ponto 1: "))
g1 = int(input("Informe a longitude do ponto 1: "))

t2 = int(input("Informe a latitude do ponto 2: "))
g2 = int(input("Informe a longitude do ponto 2: "))
#converter graus para radianos
t1 = math.radians(t1)
g1 = math.radians(g1)

t2 = math.radians(t2)
g2 = math.radians(g2)

#calcular a distância e converter a distancia para string
distancia = 6371.01 * math.acos(math.sin(t1)*math.sin(t2) + math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
distancia = str(distancia)

print("A distância é de: " +distancia+" quilômetros")
