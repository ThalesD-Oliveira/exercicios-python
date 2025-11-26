seg1 = int(input("Digite o comprimento do primeiro segmento: "))
seg2 = int(input("Digite o comprimento do segundo segmento: "))
seg3 = int(input("Digite o comprimento do terceiro segmento: "))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print("Os segmentos podem formar um triângulo.")
    if seg1 == seg2 == seg3:
        print("Tipo: Equilátero")
    elif seg1 != seg2 != seg3 != seg1:
        print("Tipo: Escaleno")
    else:
        print("Tipo: Isósceles")
else:
    print("Os segmentos não podem formar um triângulo.")