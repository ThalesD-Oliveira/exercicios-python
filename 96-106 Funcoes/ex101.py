"""
DESAFIO 101:
Crie um programa que tenha uma função chamada voto() que vai receber 
como parâmetro o ano de nascimento de uma pessoa, retornando um valor 
literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO 
nas eleições.
"""

def voto(ano_nascimento):
    """
    Analisa a idade com base no ano de nascimento e retorna o status do voto.
    """
    from datetime import date
    
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa Principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))