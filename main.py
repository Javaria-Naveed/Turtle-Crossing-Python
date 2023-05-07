import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pale Green")
screen.title("Help Turtle Get Across")
screen.tracer(0)

turtle = Turtle()
turtle.penup()
turtle.shape("square")
turtle.color("Light Gray")
turtle.shapesize(stretch_wid=26, stretch_len=30)

turtle_1 = Turtle()
turtle_1.penup()
turtle_1.goto(0, 260)
turtle_1.shape("square")
turtle_1.color("Black")
turtle_1.shapesize(stretch_wid=0.3, stretch_len=30)

turtle_2 = Turtle()
turtle_2.penup()
turtle_2.goto(0, -260)
turtle_2.shape("square")
turtle_2.color("Black")
turtle_2.shapesize(stretch_wid=0.3, stretch_len=30)

turtle_3 = Turtle()
turtle_3.penup()
turtle_3.goto(0, 0)
turtle_3.shape("square")
turtle_3.color("Black")
turtle_3.shapesize(stretch_wid=0.5, stretch_len=7)

turtle_4 = Turtle()
turtle_4.penup()
turtle_4.goto(300, 0)
turtle_4.shape("square")
turtle_4.color("Black")
turtle_4.shapesize(stretch_wid=0.5, stretch_len=7)

turtle_5 = Turtle()
turtle_5.penup()
turtle_5.goto(-300, 0)
turtle_5.shape("square")
turtle_5.color("Black")
turtle_5.shapesize(stretch_wid=0.5, stretch_len=7)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

scoreboard.update_scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
