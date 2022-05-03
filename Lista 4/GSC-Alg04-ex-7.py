#Aproximação de pi

i = 4
total = 3
n = 0
while n < 15:
    if n%2 == 0: 
        aprox = 4/((i-2)*(i-1)*i)
        total = total + aprox
        print(f"A aproximação {n} é de {total}")
    else:
        aprox = 4/((i-2)*(i-1)*i)
        total = total - aprox
        print(f"A aproximação {n} é de {total}")
    i = i + 2
    n += 1

else:
    print(total, "É a aproximação final")
    