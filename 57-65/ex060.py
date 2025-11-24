from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))

# Outra forma de fazer o fatorial sem usar a biblioteca math
# f = 1
# for i in range(1, n + 1):
#     f *= i
# print('O fatorial de {} é {}.'.format(n, f))

# Outra forma de fazer o fatorial sem usar a biblioteca math e usando while
# f = 1
# c = n
# while c > 0:
#     f *= c
#     c -= 1
# print('O fatorial de {} é {}.'.format(n, f))

