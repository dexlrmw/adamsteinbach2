# introduction to turtles
# feb 11
# created by dillon weech
# spirograph
'''
from turtle import *

# import turtle
color('purple', 'red')
begin_fill()
while True:
    forward (200)
    left (170)
    if abs(pos()) <1:
        break
end_fill ()
done()

'''

import turtle
loadWindow = turtle.Screen()
turtle.speed(11)

for i in range (100):
    turtle.circle (5*i)
    turtle.circle (-5*i)
    turtle.circle (-50*i)
    turtle.left (0.5)
turtle.exitonclick()