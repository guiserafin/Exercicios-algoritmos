dB = int(input('Insira a intensidade do barulho em decibeis: '))

if (dB < 40):
    print('Menos decibeis que uma sala silenciosa')
elif (dB == 40):
    print('Decibeis iguais ao de uma sala silenciosa')
elif(dB > 40 and dB < 70):
    print('Volume sonoro entre uma sala silenciosa e um despertador')
elif(dB == 70):
    print('Volume sonoro de um despertador')
elif (dB > 70 and dB < 106):
    print('Volume sonoro entre um despertador e um cortador de grama')
elif (dB == 106):
    print('Volume de um cortador de grama')
elif (dB > 106 and dB < 130):
    print('Volume entre um cortador de grama e uma britadeira')
elif (dB == 130):
    print('Tanto barulho quanto uma britadeira')
else:
    print('Som mais alto que de uma britadeira')