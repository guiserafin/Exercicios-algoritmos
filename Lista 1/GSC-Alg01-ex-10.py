from cmath import log10

a = int(input("Determine o valor de a: "))
b = int(input("Determine o valor de b: "))

soma      = a + b
diferença = b - a
produto   = a*b
quociente = a/b
resto     = a%b
log       = log10(a)
potencia  = a**b

print('soma: ',soma)
print('diferença: ',diferença)
print('produto: ',produto)
print('quociente: ', quociente)
print('resto: ' ,resto)
print('logaritmo de a na base 10: ', log)
print('a elevado a b: ', potencia)
