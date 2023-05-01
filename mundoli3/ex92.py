data = {}
while True:
    data['name'] = str(input('Enter your name: '))
    data['born'] = int(input('Enter your year of birth: '))
    data['work'] = int(input('Enter your work card (Dont have? Type 0): '))
    if data['work'] == 0:
        break
    else:
        data['hire'] = int(input('Enter your year of hire: '))
        data['salary'] = int(input('Enter your salary: R$'))
        data['apo'] = (data['hire'] - data['born']) + 45
    break
for k,v in data.items():
    print(f"{k}: {v};")
# n sei calcular aposentadoriakkk