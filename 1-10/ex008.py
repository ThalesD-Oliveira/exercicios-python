medida = float(input('Digite uma distância em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'''
A medida de {medida}m corresponde a:
{km} km
{hm} hm
{dam} dam
{dm} dm
{cm} cm
{mm} mm
''')

'''print('A media de {}m correspondente a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))
'''