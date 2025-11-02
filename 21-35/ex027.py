n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

print(f'Muito prazer em te conhecer, {n}!')
print(f'Seu primeiro nome é \033[1m{nome[0]}\033[m')
print(f'Seu múltimo nome é \033[1m{nome[len(nome)-1]}\033[m')
