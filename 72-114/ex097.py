"""
DESAFIO 097:
Faça um programa que tenha uma função chamada escreva(), que receba 
um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""

def escreva(msg):
    """
    Exibe uma mensagem centralizada entre linhas adaptáveis ao tamanho do texto.
    :param msg: O texto a ser exibido.
    """
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')