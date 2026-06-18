"""
DESAFIO 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for 
diferente de ZERO, o dicionário receberá também o ano de contratação 
e o salário. Calcule e acrescente, além da idade, com quantos anos 
a pessoa vai se aposentar.
"""

from datetime import datetime

dados = dict()

# Coleta de dados básicos
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# Coleta de dados adicionais se houver CTPS
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    
    # Cálculo da aposentadoria:
    # (Ano de contratação + 35 anos de contribuição) - Ano de nascimento = idade da aposentadoria
    idade_aposentadoria = (dados['contratação'] + 35) - nasc
    dados['aposentadoria'] = idade_aposentadoria

print('-=' * 30)

# Exibição organizada dos dados
for k, v in dados.items():
    if k == 'salário':
        print(f' - {k.capitalize()}: R${v:.2f}')
    else:
        print(f' - {k.capitalize()}: {v}')