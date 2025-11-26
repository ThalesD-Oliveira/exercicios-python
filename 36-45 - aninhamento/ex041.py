from datetime import date
atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento?'))
idade = atual - nasc
print('O atleta tem {} anos de idade'.format(idade))

if idade <= 9:
    print('O atleta é MIRIM')
elif idade <= 14:
    print('O atleta é INFANTIL')
elif idade <= 19:
    print('O atleta é JUNIOR')
elif idade <= 25:
    print('O atleta é SÊNIOR')
else:
    print('O atleta é MASTER')