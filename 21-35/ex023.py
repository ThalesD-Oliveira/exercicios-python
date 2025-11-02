num = int(input('Informe um número: '))
u = num // 1 % 100
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}' if d > 0 else 'Dezena: 0')
print(f'Centena: {c}' if c > 0 else 'Centena: 0')
print(f'Milhar: {m}' if m > 0 else 'Milhar: 0')


