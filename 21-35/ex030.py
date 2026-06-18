num = int(input('Digite um número inteiro: '))

# O resto da divisão de qualquer número par é 0
# O resto da divisão de qualquer número ímpar é 1
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')