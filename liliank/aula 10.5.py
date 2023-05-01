ano = int(input('O ano que vc quer analisar: '))
dec = ano % 4
if dec == 0:
    print('esse ano é bissexto')
else:
    print('esse ano nao é bissexto')
