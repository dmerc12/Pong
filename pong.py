import platform
import winsound
import turtle
import time
import os

# initialize score
player1_score = 0
player2_score = 0

# take winning score input
winning_score = int(input('What score would you like to play to?    '))

# window
window = turtle.Screen()
window.title('PONG')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape('square')
left_paddle.color('white')
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape('square')
right_paddle.color('white')
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.x_speed = 0.02
ball.y_speed = 0.02

# score
score = turtle.Turtle()
score.speed(0)
score.color('white')
score.penup()
score.hideturtle()
score.goto(0, 260)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 150)

# function to move left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    if y < 250:
        y += 20
    left_paddle.sety(y)

# function to move left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    if y > -240:
        y -= 20
    left_paddle.sety(y)

# function to move right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    if y < 250:
        y += 20
    right_paddle.sety(y)

# function to move right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    if y > -240:
        y -= 20
    right_paddle.sety(y)

# function to write score
def write_score():
    score.clear()
    score.write(f'Player 1: {player1_score}  Player 2: {player2_score}', align='center', font=('Courier', 24, 'normal'))

# function to play sound
def play_sound():
    if platform.system() == 'Darwin':
        os.system('afplay bounce.wav&')
    elif platform.system() == 'Windows':
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    elif platform.system() == 'Linux':
        os.system('aplay bounce.wav&')

# function to check win
def check_win():
    write_score()
    if player1_score == winning_score:
        ball.x_speed = 0
        ball.y_speed = 0
        pen.clear()
        pen.write('Player 1 Wins!', align='center', font=('Courier', 24, 'normal'))
    elif player2_score == winning_score:
        ball.x_speed = 0
        ball.y_speed = 0
        pen.clear()
        pen.write('Player 2 Wins!', align='center', font=('Courier', 24, 'normal'))
    else:
        time.sleep(2)

# keyboard binding
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

# main game loop
while True:
    window.update()
    write_score()

    ## move the ball
    ball.setx(ball.xcor() + ball.x_speed)
    ball.sety(ball.ycor() + ball.y_speed)

    ## border checking
    ### top border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.y_speed *= -1
        play_sound()

    ### bottom border bounce
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.y_speed *= -1
        play_sound()

    ### right border catch
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.x_speed *= -1
        player1_score += 1
        check_win()

    ### left border catch
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.x_speed *= -1
        player2_score += 1
        check_win()

    ## paddle and ball collisions
    ### left paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.x_speed *= -1
        play_sound()

    ### right paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.x_speed *= -1
        play_sound()
