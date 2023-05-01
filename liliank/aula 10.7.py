slr = float(input('Digite seu salário em reais: '))
a1 = slr * 10/100
a2 = slr * 15/100

if slr > 1250:
    print('Seu aumento é de {:.1f}\nLogo, seu salário agora é {}'.format(a1, a1 + slr))
else:
    print('Seu aumento é de {:.1f}\nLogo, seu salário será {}'.format(a2, a2 + slr))