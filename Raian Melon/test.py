kosarica = {}

kosarica['jabuka'] = 15
kosarica['sljive'] = 23
kosarica['mandarine'] = 3

print(kosarica)

kosarica['jabuka'] += 15

print(kosarica)

broj_mandarina = kosarica['mandarine']
print('mandarine', broj_mandarina)\

trazim_voce = 'kruske'
if trazim_voce in kosarica: 
    broj_voca = kosarica[trazim_voce]
    print('kruske', broj_voca)
else:
    print('nemamo', trazim_voce)
