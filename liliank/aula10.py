n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))
m = (n1 + n2)/2

if m >= 8:
    print('aluno aprovado')
else:
    print('aluno reprovado')
print('média = {}'.format(m))