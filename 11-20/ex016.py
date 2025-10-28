from math import trunc 
'''import math''' 

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
'''trunc - remove todos os números após a vírgula '''
'''print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num))) ''' 


'''---------------------------------------------------'''

'''Usando apenas a função int(), sem importar a biblioteca math'''
'''num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')'''