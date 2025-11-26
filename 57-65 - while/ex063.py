print('-'*30)
print('Sequência de fibonatti')
print('-'*30)

n = int(input('Quantos números você quer mostrar?'))

t1 = 0
t2 = 1
cont = 3
print('~'*30)
print(f'{t1} -> {t2}', end='')

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1 # cont = cont + 1  |  incremento
print(' -> FIM')
print('~'*30)

# Exemplo de saída:
# 0  -  1  -  1  -  2  -  3  -  5  -  8  -  13  -  21  -  34  -  55  - 89
# t1 -  t2 -  t3
#       t1 -  t2 -  t3
#             t1 -  t2 -  t3
#                   t1 -  t2 -  t3
