veloc = float(input('diga a velocidade do movel (em km/h):'))
if veloc > 80:
    multa = (veloc - 80) * 7
    print('MULTADO!\nPague imediatamente {:.2f} reais!'.format(multa))
else:
    print('Bom trajeto! Dirija com cuidado.')