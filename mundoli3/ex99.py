from time import sleep
def jojo(lst):
    print('-=-'*20)
    print(f'The list is: {lst};')
    lst.sort(reverse=True)
    print(f'It contains {len(lst)} numbers and the biggest is {lst[0]};')
    sleep(0.5)
lst = [23, 25, 30]
jojo(lst)
lst = [-4, -3, -2, -1]
jojo(lst)
lst = [19, 18, 22, 1, 2, 3, 4, 5, 6, 7, 8]
jojo(lst)
print('-=-'*20)