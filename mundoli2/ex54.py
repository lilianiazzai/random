major = 0
minor = 0
for age in range(1, 3):
    age = int(input('In which year you were born? '))

    if age > 2004:
        print('You are minor')
        minor = minor + 1

    else:
        print('You are major')
        major = major + 1
print('------' * 20)
print('In total: \n{} people are minor; \n{} people are major'.format(minor, major))