import turtle
import random

screen = turtle.Screen()
screen.title("Race")
screen.setup(width=800, height=600)
screen.bgpic("background.jpg")
is_race_on  = False
user_bet = screen.textinput(title="Make your bet",prompt =
"Which turtle will win the race? Enter a color:(white/blue/green/yellow/orange/purple")

turtles = []

y_list = [-170,-120,-70,-20,30,80]
color = ["white","blue","green","yellow","orange","purple"]

for i in range(0, 6):
    timmy = turtle.Turtle()
    timmy.color(color[i])
    timmy.shape("turtle")
    timmy.shapesize(1.5)
    timmy.penup()
    timmy.goto(-390, y_list[i])
    turtles.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 390:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! {turtle.pencolor()} is the winner!")
                is_race_on = False
            else:
                print(f"You lose! {turtle.pencolor()} is the winner!")
                is_race_on = False

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
