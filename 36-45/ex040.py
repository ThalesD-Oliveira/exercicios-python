nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media < 5:
    print("Reprovado")
elif 5 <= media < 7:
    print("Recuperação")
elif media >= 7:
    print("Aprovado")