# my class example for Functions
# really simple function
'''
def f(x):
    # a one line function
    return x **2+10

#out of function into main program

x = 3
print ('Results of my calculation are: ', f(x))

# slightly more complex example, but still basic
'''
num = input('please enter a day in the form first to twelfth: ')
print ('on the ')
def song(day):
    if (day == 'third'):
        print ('three french hens, ', song('second'))
    if (day == 'second'):
        print ('two turtle doves, and', song ('first'))
    if (day == 'first'):
        print ('a partridge in a pear tree. ')

# main program for running my function
# ask user for input

#num = input('please enter a day in the form first to twelfth: ')
#print ('On the ', num, 'day of christmas my true love gave to me', song(num))

'''
#import array library
from array import *

my_array = array('i', [1,2,3,4])
print (my_array)
'''

# slightly different
'''
import array as arr
a = arr.array('d', [1, 3.5, 7.9])
print(a)
print('first element ', a[0])
print('second element ', a[1])
print('last element', a[-1])
'''

