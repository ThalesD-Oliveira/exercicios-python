"""
DESAFIO 095:
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento 
de cada jogador.
"""

time = list()

while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    
    partidas = list()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador)
    
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

# Tabela de visualização
print('-=' * 30)
print(f"{'cod':<4} {'nome':<15} {'gols':<15} {'total':<10}")
print('-' * 45)
for i, v in enumerate(time):
    print(f"{i:<4} {v['nome']:<15} {str(v['gols']):<15} {v['total']:<10}")
print('-' * 45)

# Sistema de busca
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 45)

print('<< VOLTE SEMPRE >>')