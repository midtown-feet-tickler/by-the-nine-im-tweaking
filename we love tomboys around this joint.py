from turtle import *

speed(100)


def square(side):
    for i in range(4):
        fd(side)
        lt(90)


# penup()
# bk(105)
# pendown()

def rectangle(side):
    for i in range(2):
        fd(3 * side)
        lt(90)
        fd(2 * side)
        lt(90)


#  penup()
#  bk(105)
# pendown()
def rhombus(side):
    for i in range(2):
        fd(3 * side)
        lt(135)
        fd(3 * side)
        lt(45)


def triangle(side):
    fd(3 * side)
    lt(135)
    fd(2 * side)
    lt(90)
    fd(2 * side)


for i in range(1, 1000, 4):
   triangle(i)

done()
