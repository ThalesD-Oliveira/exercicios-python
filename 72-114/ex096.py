"""
DESAFIO 096:
Faça um programa que tenha uma função chamada área(), que receba 
as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.
"""

def area(larg, comp):
    """
    Calcula e exibe a área de um terreno retangular.
    :param larg: largura do terreno em metros
    :param comp: comprimento do terreno em metros
    """
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.2f}m².')

# Programa principal
print('  CONTROLE DE TERRENOS')
print('-' * 25)

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

area(l, c)