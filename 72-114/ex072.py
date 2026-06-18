cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
        'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 
        'dezenove', 'vinte')

print("--- Digite um número de 0 a 20 (ou '-' para sair) ---")

while True:
    # 1. Lemos a entrada como texto (string)
    entrada = input('>>> ')
    
    # 2. Verificamos se o usuário quer sair
    if entrada == '-':
        print('Programa encerrado pelo usuário.')
        break
    
    # 3. Tentamos converter apenas se não for o comando de saída
    try:
        num = int(entrada)
        
        # 4. Validamos o intervalo
        if 0 <= num <= 20:
            print(f'Você digitou o número {cont[num]}')
        else:
            print('Erro: O número deve estar entre 0 e 20!')
            
    except ValueError:
        print('Erro: Por favor, digite um número inteiro válido ou "-" para sair.')