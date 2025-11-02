distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f} km.')

# Operador ternário | variável atribui duas condições
preco = distancia * 0.50 if distancia <=200 else distancia * 0.45
print(f'O preço da sua passagem será de R$ {preço:.2f}.')


'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''