"""
Unidades de tempo (novamente). Neste exercício você deve fazer o processo inverso do
exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de
tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na
forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos
respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com
dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10.

"""
segundosUsuario = int(input("Insira a quantidade de segundos: "))

dias     = segundosUsuario // 86400
horas    = (segundosUsuario % 86400) // 3600
minutos  = ((segundosUsuario % 86400) % 3600) // 60
segundos = ((segundosUsuario % 86400) % 3600) % 60

if segundos < 10 :
    segundos = '0' + str(segundos)


print(dias,"dias", horas,"horas", minutos,"minutos", segundos,"segundos")


