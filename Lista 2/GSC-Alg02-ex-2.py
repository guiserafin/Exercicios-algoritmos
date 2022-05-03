"""
Unidades de tempo (novamente). Neste exercício você deve fazer o processo inverso do
exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.

"""
segundos = int(input("Insira a quantidade de segundos: "))

dias = 0
horas = 0
minutos = 0
segundos2 = 0

if segundos >= 86400:
    resto1 = segundos - 86400
    dias = (segundos-resto1)/86400
    if resto1 >= 3600:
        resto2 = resto1 - 3600
        horas = (resto1-resto2)/3600
        if resto2 >=60:
            resto3 = resto2 - 60
            minutos = (resto2-resto3)/60
            if resto3 !=0:
                segundos2 = resto3
        elif resto2 <60 and resto2 > 0:
            segundos2 = resto2
    elif resto1 >= 60 and resto1 < 3600:
        resto2 = resto1-60
        minutos = resto2/60
    elif resto1 <60:
        segundos2 = resto1
elif segundos >= 3600 and segundos <86400:
    resto1 = segundos - 3600
    horas = (segundos-resto1)/3600
    if resto1 >=60:
        resto2 = resto1 - 60
        minutos = (resto1-resto2)/60
        if resto2 !=0:
            segundos2 = resto2
elif segundos >= 60 and segundos <3600:
    resto1 = segundos - 60
    minutos = (segundos-resto1)/60
    if resto1 != 0:
        segundos2 = resto1
else:
    segundos2 = segundos

print(dias,"dias", horas,"horas", minutos,"minutos", segundos2,"segundos")


