from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O seno de {angulo} é {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O cosseno de {angulo} é {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'A tangente de {angulo} é {tangente:.2f}')