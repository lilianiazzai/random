li = []
for c in range(0,5):
    num = int(input('Enter a number: '))
    if c == 0 or num > li[-1]:
        li.append(num)
    else:
        pos = 0
        while pos < len(li):
            if num <= li[pos]:
                li.insert(pos, num)
                break
            pos += 1
print(li)