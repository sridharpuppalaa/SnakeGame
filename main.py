from turtle import *

root = Screen()
root.title("Snake Game")
root.setup(width=600, height=600)

root.bgcolor("pink")
root.bgpic("border.gif")
root.addshape('upmouth.gif')
root.addshape('food.gif')
root.addshape('body.gif')

head = Turtle()
head.shape("upmouth.gif")
head.penup()
head.goto(0, 0)

food = Turtle()
food.shape("food.gif")
food.penup()
food.goto(0, 150)


text = Turtle()
text.penup()
text.goto(0, 268)



while True:
    root.update()
