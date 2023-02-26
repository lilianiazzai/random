# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# a média de idade do grupo; 
# qual é o nome do homem mais velho; 
# quantas mulheres têm menos de 20 anos.

soma = 0
older = 0
count = 0
nameold = ''
for c in range(1, 5):
    name = str(input('{}.Name: '.format(c)))
    age = int(input('{}.Age: '.format(c)))
    gender = int(input('(1)Male \n(2)Female \n{}.Gender: '.format(c)))
    print('^^^^^' * 20)
    soma += age

    if gender == 1:
        if c == 1:
            older = age
            nameold = name
        else:
            if age>older:
                older = age
                nameold = name

    if gender == 2 and age < 20:
       count = count + 1
print('The average age in the group is {};'.format(soma // c))
print('The oldest man is {} years and his name is {};'.format(older, nameold))
print('There are {} women with age lower than 20 years;'.format(count))