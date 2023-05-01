stu = {}
peo = str(input('Enter students name: '))
stu['student'] = peo
ave = float(input('Enter students average: '))
stu['average'] = ave
print('...'*20)
print(f"Student's name: {stu['student']}")
print(f"Student's average: {stu['average']}")
if ave >= 7:
    print(f"{stu['student']} is aproved!")
else:
    print(f"{stu['student']} is disaproved :(( ")
print('...'*20)