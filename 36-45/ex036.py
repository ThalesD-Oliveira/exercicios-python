casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3

print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(casa, anos), end=' ')
print('a prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')