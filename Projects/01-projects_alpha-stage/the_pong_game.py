"""
Developer; Sam Skywalker
Purpose; The Pong game in Python
Data; 12022.01.10.17:25

"""

import turtle as tr
from pyfiglet import *



# Initiate the window...
win = tr.Screen()
win.title("The Pong Game by @skywalkerSam")
win.bgcolor("black")
win.setup(width=900, height=600)
win.tracer(0)    # Stops the window to reload by itself so, the gameplay'll be a bit fast ;)


# Paddle A
paddle_a = tr.Turtle()
paddle_a.speed(0)   # Max Speed ;)
paddle_a.shape("square")
paddle_a.color("#28fc03")   # HEX code of light green ;)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-400, 0)


# Paddle B
paddle_b = tr.Turtle()
paddle_b.speed(0)   
paddle_b.shape("square")
paddle_b.color("#28fc03")  
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(400, 0)


# The Ball
the_ball = tr.Turtle()
the_ball.speed(0)   
the_ball.shape("square")
the_ball.color("#28fc03")  
the_ball.penup()
the_ball.goto(0, 0)
    # Ball movement...
the_ball.dx = 0.2
the_ball.dy = -0.2


# Movement functions()
# paddle_a
def pa_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)


def pa_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)


# paddle_b
def pb_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def pb_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)



# Keys Implementation
win.listen()
win.onkeypress(pa_up, "w")
win.onkeypress(pa_down, "s")
win.onkeypress(pb_up, "Up")
win.onkeypress(pb_down, "Down")



# Intro...
pong_intro = figlet_format(" The  Pong  Game ", font="big")
print(pong_intro)

# Main Game Loop...
while (True):
    win.update()

    # Move the Ball...
    the_ball.setx(the_ball.xcor() + the_ball.dx)
    the_ball.sety(the_ball.ycor() + the_ball.dy)

    # Border Implementation...
    if (the_ball.ycor() > 290):
        the_ball.sety(290)
        the_ball.dy *= -1
    
    if (the_ball.xcor() > 440):
        the_ball.goto(0, 0)
        the_ball.dx *= -1

    if (the_ball.ycor() < -290):
        the_ball.sety(-290)
        the_ball.dy *= -1

    if (the_ball.xcor() < -440):
        the_ball.goto(0, 0)
        the_ball.dx *= -1


    # paddles and the ball collisions...
    




