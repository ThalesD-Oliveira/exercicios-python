"""
DESAFIO 099:
Faça um programa que tenha uma função chamada maior(), que receba 
vários parâmetros com valores inteiros. Seu programa tem que 
analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep

def maior(* núm):
    print('-=' * 15)
    print('Analisando os valores passados...')
    
    if len(núm) == 0:
        print('Foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')
    else:
        for valor in núm:
            print(f'{valor} ', end='', flush=True)
            sleep(0.3)
        print(f'Foram informados {len(núm)} valores ao todo.')
        print(f'O maior valor informado foi {max(núm)}.')

# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()