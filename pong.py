import turtle

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
