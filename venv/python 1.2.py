# Grade 10 review examples
# feb 11
# Dillon Weech
# print all letters except i, c and s

for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter == 'i' or letter == 'c' or letter == 's':
        continue
    print ('current letter is: ', letter)
    var=26

# next example
# set count to 0, this is the precondition to our while

count = 0

while(count<3):
    count = count + 1
    print('run', count, 'times')