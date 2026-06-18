salario = float(input('Qual é o salário atual do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(f'O salário do funcionário de R${salario:.2f}, após aumento, será de R${novo:.2f}.')