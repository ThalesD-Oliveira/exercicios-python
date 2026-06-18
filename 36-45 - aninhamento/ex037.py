num = int(input("Digite um número inteiro: "))
print('''Escolha uma das bases para conversão:
      [ 1 ] convert para BINÁRIO
      [ 2 ] convert para OCTAL
      [ 3 ] convert para HEXADECIMAL''')
opção = int(input("Sua opção: "))

# [2:] - começa da posição 2 e vai até o final da string, ignorando os dois primeiros caracteres que indicam o tipo da base

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')