
dias_alugados = int(input('Quantidade de dias em que o carro foi alugado: '))
km_percorridos = float(input('Quantidade de kms percorridos: '))
preco = (dias_alugados * 60) + (km_percorridos * 0.15)

print(f'O total a pagar é de R${preco:.2f}.')