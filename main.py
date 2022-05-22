from turtle import *
import time
import random
from pygame import mixer

score = 0
exec_delay = 0.2

root = Screen()
root.title("Snake Game")
root.setup(width=600, height=600)
root.tracer(False)

root.bgcolor("pink")
root.bgpic("border.gif")
root.addshape('upmouth.gif')
root.addshape('downmouth.gif')
root.addshape('rightmouth.gif')
root.addshape('leftmouth.gif')
root.addshape('food1.gif')
root.addshape('body.gif')

head = Turtle()
head.shape("upmouth.gif")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

food = Turtle()
food.shape("food1.gif")
food.penup()
food.goto(0, 150)

text = Turtle()
text.penup()
text.goto(0, 268)
text.hideturtle()
text.color("White")
text.write("Score: 0", font=("courier", 24, "bold"), align="center")

lost = Turtle()
lost.penup()
lost.goto(0, 0)
lost.hideturtle()
lost.color("red")


def move_snake():
    if head.direction == 'up':
        y = head.ycor()
        y += 20
        head.sety(y)

    if head.direction == 'down':
        y = head.ycor()
        y -= 20
        head.sety(y)

    if head.direction == 'right':
        x = head.xcor()
        x += 20
        head.setx(x)

    if head.direction == 'left':
        x = head.xcor()
        x -= 20
        head.setx(x)

def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.shape("upmouth.gif")

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.shape("downmouth.gif")

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.shape("rightmouth.gif")

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.shape("leftmouth.gif")


root.listen()

root.onkeypress(go_up, "Up")
root.onkeypress(go_down, "Down")
root.onkeypress(go_right, "Right")
root.onkeypress(go_left, "Left")
segments = []

while True:
    root.update()

    if head.xcor() > 260 or head.xcor() < -260 or head.ycor() > 260 or head.ycor() < -260:
        lost.write("Game Lost", font=("courier", 24, "bold"), align="center")
        mixer.init()
        mixer.music.load("out.mp3")
        mixer.music.play()

        time.sleep(1)
        lost.clear()
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for body in segments:
            body.goto(1000, 1000)

        segments.clear()
        score = 0
        exec_delay = 0.2
        text.clear()
        text.write(f"Score: 0", font=("courier", 24, "bold"), align="center")



    if head.distance(food) < 20:
        mixer.init()
        mixer.music.load("eat.mp3")
        mixer.music.play()

        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        body = Turtle()
        body.penup()
        body.shape("body.gif")

        exec_delay -= 0.005

        segments.append(body)
        score = score + 10
        text.clear()
        text.write(f"Score:{score}", font=("courier", 24, "bold"), align="center")


    for i in range(len(segments) - 1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move_snake()

    for body in segments:
        if body.distance(head) < 20:

            lost.write("Game Lost", font=("courier", 24, "bold"), align="center")
            mixer.init()
            mixer.music.load("out.mp3")
            mixer.music.play()

            time.sleep(1)
            lost.clear()
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in segments:
                body.goto(1000, 1000)

            segments.clear()
            score = 0
            exec_delay = 0.2
            text.clear()
            text.write(f"Score: 0", font=("courier", 24, "bold"), align="center")


    time.sleep(exec_delay)
