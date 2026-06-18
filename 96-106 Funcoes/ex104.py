"""
DESAFIO 104:
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
semelhante à função input() do Python, só que fazendo a validação para 
aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(msg):
    """
    Solicita uma entrada do usuário e valida se é um número inteiro.
    :param msg: A mensagem que será exibida ao usuário.
    :return: O valor inteiro validado.
    """
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')