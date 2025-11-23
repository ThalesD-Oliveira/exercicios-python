from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('O computador escolheu {}'.format(itens[computador]))

print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogada = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(0.5)
print('-=' * 11)

print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogada]))
print('-=' * 11)
if computador == 0:  # computador jogou PEDRA
    if jogada == 0:
        print('EMPATE')
    elif jogada == 1:
        print('JOGADOR VENCE')
    elif jogada == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
        
elif computador == 1:  # computador jogou PAPEL
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print('EMPATE')
    elif jogada == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
        
elif computador == 2:  # computador jogou TESOURA
    if jogada == 0:
        print('JOGADOR VENCE')
    elif jogada == 1:
        print('COMPUTADOR VENCE')
    elif jogada == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
