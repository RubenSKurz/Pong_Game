from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()

player_r = Paddle()
player_r.start_position(0)
player_l = Paddle()
player_l.start_position(1)


screen.listen()
screen.onkey(player_r.paddle_up, "Up")
screen.onkey(player_r.paddle_down, "Down")
screen.onkey(player_l.paddle_up, "w")
screen.onkey(player_l.paddle_down, "s")

speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
        pass
    if ball.distance(player_r) < 50 and ball.xcor() > 320 or ball.distance(player_l) < 50 and ball.xcor() < -320:
        speed *= 0.9
        ball.bounce_x()
        pass
    if ball.xcor() > 380:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        speed = 0.1
        ball.restart_ball()
        pass
    if ball.xcor() < -380:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        speed = 0.1
        ball.restart_ball()

screen.exitonclick()
