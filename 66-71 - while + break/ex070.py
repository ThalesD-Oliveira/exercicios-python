while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    if preco > 1000:
        totmil += 1
    if preco < menor or total == 0:
        menor = preco
        barato = produto
    resp =' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total gasto na compra: R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')