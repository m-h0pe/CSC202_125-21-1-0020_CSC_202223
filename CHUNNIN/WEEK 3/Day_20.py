
from turtle import Screen, Turtle

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake game")

segments=[]

starting_positions= [(0,0), (-20,0), (20,0)]
for postion in starting_positions:

    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(postion)

game_on= True
while game_on:
    for seg in segments:
        seg.forward(28)








screen.exitonclick()

