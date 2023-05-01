perc = int(input('Quantos km tem o seu percursso? '))
if perc <= 200:
    valor = perc * 0.5
    print('A sua passagem custará {} reais.'.format(valor))
else:
    valor = perc * 0.45
    print('A sua passagem custará {} reais.'.format(valor))
print('Tenha um bom dia! Agradecemos o contato!')