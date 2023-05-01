biggest = 0
smallest = 0
for w in range (1, 6):
    weight = int(input('person {} weight(kg): '.format(w)))
    if w == 1:
        biggest = weight
        smallest = weight
    else:
        if weight > biggest:
            biggest = weight
        if weight < smallest:
            smallest = weight
print('The biggest weight readen was {}kg and the smallest was {}kg;'.format(biggest, smallest))

