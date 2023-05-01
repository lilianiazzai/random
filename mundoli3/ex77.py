li = ('Lilian', 'Iazzai', 'Souza', 'Oliveira', 'Valeria', 'Almeida', 'Vanessa', 'Mach')
for c in li:
    print(f'\nIn the word {c} we have ', end = '')
    for letter in c:
        if letter.lower() in 'aiueo':
            print(f'"{letter}"', end = '')