print('=' * 18)
print(' TEMOSOS UMA OFERTA! ')
print('=' * 18)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')