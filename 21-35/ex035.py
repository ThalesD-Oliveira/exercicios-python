'''' Regra dos três lados
A soma do comprimento de dois lados deve ser sempre maior que o comprimento do terceiro lado. Ou seja, para lados a, b, c:
a + b > c
a + c > b
b + c > a
Se qualquer uma dessas não for verdadeira, não forma triângulo.'''

print('-=' * 20)
print('Digite o comprimento de três segmentos para verificar se eles podem formar um triângulo.')
print('-=' * 20)

a = float(input('Digite o comprimento do primeiro lado: '))
b = float(input('Digite o comprimento do segundo lado: '))
c = float(input('Digite o comprimento do terceiro lado: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos formam um triângulo.')
else:
    print('Os segmentos não formam um triângulo.')