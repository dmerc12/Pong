import turtle

# initialize score
player1_score = 0
player2_score = 0

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

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player 1: {player1_score}  Player 2: {player2_score}', align='center', font=('Courier', 24, 'normal'))

# function to move left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# function to move left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# function to move right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# function to move right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


# keyboard binding
window.listen()
window.onkeypress(left_paddle_up, 'w')
window.onkeypress(left_paddle_down, 's')
window.onkeypress(right_paddle_up, 'Up')
window.onkeypress(right_paddle_down, 'Down')

# main game loop
while True:
    window.update()

    ## move the ball
    ball.setx(ball.xcor() + ball.x_speed)
    ball.sety(ball.ycor() + ball.y_speed)

    ## border checking
    ### top border bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.y_speed *= -1

    ### bottom border bounce
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.y_speed *= -1

    ### right border catch
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.x_speed *= -1
        player1_score += 1
        pen.clear()
        pen.write(f'Player 1: {player1_score}  Player 2: {player2_score}', align='center', font=('Courier', 24, 'normal'))

    ### left border catch
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.x_speed *= -1
        player2_score += 1
        pen.clear()
        pen.write(f'Player 1: {player1_score}  Player 2: {player2_score}', align='center', font=('Courier', 24, 'normal'))

    ## paddle and ball collisions
    ### left paddle collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)
        ball.x_speed *= -1

    ### right paddle collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)
        ball.x_speed *= -1
