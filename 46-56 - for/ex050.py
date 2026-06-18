soma = 0
contador = 0
for c in range(1, 7):
    num = int(input("Digite o {} valor : ".format(c)))
    if num % 2 == 0:
        soma += num  # soma = soma + num
        contador += 1  # contador = contador + 1
print("Você informou {} números pares e a soma foi {}".format(contador, soma))