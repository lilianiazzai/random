sent = str(input('Type a sentence: '))
edit = sent.strip().upper().split()
edit2 = ''.join(edit)
inverse = ''
for word in range(len(edit2) - 1, -1, -1):
    inverse += edit2[word]

if inverse == edit2:
    print('The sentence "{}" is a palindrome'.format(sent))
else:
    print('The sentence "{}" is not a palindrome'.format(sent))