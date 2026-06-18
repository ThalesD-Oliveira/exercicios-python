vel = float(input('Qual é a velocidade atual do carro? '))
if vel > 80:
  print(f'\033[1;31mVocê foi multado!\033[m Você excedeu o limite permitido de 80km/h.')
  multa = (vel - 80) * 7
  print(f'O valor da multa é de {multa:.2f} reais.')
print('Tenha um bom dia! Dirija com segurança!')