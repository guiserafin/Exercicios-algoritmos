#Tabela de conversão de temperaturas
#Temperatura em Fahrenheit = (TC * 9/5) + 32

temp_celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

i = 0
print("°C", "°F")
for temperatura in temp_celsius:
    temp_fahrenheit = (temp_celsius[i] * 9/5) + 32
    print(temp_celsius[i], temp_fahrenheit)
    i += 1
