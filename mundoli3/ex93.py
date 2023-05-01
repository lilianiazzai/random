from time import sleep
soc = dict()
tot = 0
soc['name'] = str(input('Enter your name: '))
soc['matches'] = int(input('Matches you played: '))
for c in range(1, soc['matches'] + 1):
    soc[f'gol{c}'] = int(input(f"Gols on the {c} match: "))
    tot += soc[f'gol{c}']
print('...'*20)
for k,v in soc.items():
    print(f"{k}: {v};")
    sleep(0.3)
print(f'total: {tot}')
print('...'*20)