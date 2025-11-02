nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"SILVA" in nome.upper()}')
# 'Silva' in nome - procura a string 'Silva' dentro da variável nome, retornando True ou False