resp = 'S'
soma = cont = media = 0
maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print('Você digitou {:.2f} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {:.2f} e o menor foi {:.2f}'.format(maior, menor))