import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
    	if car.distance(player) < 20:
    		game_is_on = False
    		scoreboard.game_over()

    #Detect a successful crossing
    if player.is_at_finish_line():
    	player.go_to_start()
    	car_manager.level_up()
    	scoreboard.increase_level()


screen.exitonclick()


#A turtle moves forward when you press the "Up" key. It can only move forwards, not back, left or right.
#Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

#1 Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
#2 Create and move the cars
#3 Detect collision with car
#4 Detect when the turtle reaches the opposite side
#5 Create scoreboard