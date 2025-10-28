from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O comprimento da hipotenusa é {hi:.2f}')

'''hi = (co**2 + ca**2) ** (1/2)'''
'''print('O comprimento da hipotenusa é {:.2f}'.format(hi))'''

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.