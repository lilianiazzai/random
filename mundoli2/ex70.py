print('~~~~MARKET KART~~~~')
prod = que = chp = ''
price = add = count = cg = che = 0
while True:
    prod = str(input('Products name: '))
    price = float(input('Products price: R$'))
    add += price
    cg += 1
    if price > 1000:
        count += 1
    if cg == 1:
        che = price
        chp = prod
    else:
        if price < che:
            price = che
            chp = prod
    que = str(input('Something more? ')).upper().strip()[0]
    while que not in 'YN':
        print('Invalid. Try again...')
        que = str(input('Something more? ')).upper().strip()[0]
    if que == 'N':
        break
print('~~' * 15)
print(f'It costs R${add};')
print(f'{count} product costs more than R$1000,0;')
print(f'The cheapest product is {chp};')
print('~~' * 15)
