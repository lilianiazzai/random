camp = ('palmeiras', 'vasco', 'chapecoense', 'flamengo', 'ponte preta', 'corinthians', 'fluminense', 'gremio', 'manaus', 'cruzeiro')
print(f'Os cinco primeiros times foram: {camp[0:5]}')
print(f'Os quatro ultimos foram: {camp[6:10]}')
print(f'Os dez primeiros, em ordem alfabetica, foram: {sorted(camp)}')
print(f'Chapecoense se encontra na posiçao {camp.index("chapecoense")}')