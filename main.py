import Paint_V2
from turtle import *
t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
step = 5
t.speed(12)
def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
def up():
    t.goto(t.xcor(), t.ycor() + step)
def down():
    t.goto(t.xcor(), t.ycor() - step)
def left():
    t.goto(t.xcor() - step, t.ycor())
def right():
    t.goto(t.xcor() + step, t.ycor())
def gray():
    t.color('gray')
def red():
    t.color('red')
def yellow():
    t.color('yellow')
def blue():
    t.color('blue')
def black():
    t.color('black')
def pink():
    t.color('pink')
def start():
    t.begin_fill()
def end():
    t.end_fill()
t.ondrag(draw)
scr = t.getscreen()
scr.onscreenclick(move)
scr.onkey(up, 'Up' )
scr.onkey(down, 'Down')
scr.onkey(left, 'Left')
scr.onkey(right, 'Right')
scr.onkey(gray, '1')
scr.onkey(red, 'R')
scr.onkey(yellow, 'Y')
scr.onkey(blue, 'T')
scr.onkey(black, 'U')
scr.onkey(pink, 'I')
scr.onkey(start, 'S')
scr.onkey(end, 'E')
scr.listen()
print('Справка: можно управлять стрелками на клавиатуре' )
