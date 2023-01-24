import turtle

win = turtle.Screen()
win.title("Pong by Nkosinathi Kelvin Ncube")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Score
score_1 = 0
score_2 = 0


# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)


# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.xspeed = 0.1
ball.yspeed = 0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player_1: 0 Player_2: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard binding
win.listen()

win.onkeypress(paddle_1_up, "w")
win.onkeypress(paddle_1_down, "s")

win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")


# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.xspeed)
    ball.sety(ball.ycor() + ball.yspeed)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.yspeed *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.yspeed *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.xspeed *=-1
        score_1 += 1
        pen.clear()
        pen.write(f"Player_1: {score_1} Player_2: {score_2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.xspeed *=-1
        score_2 += 1
        pen.clear()
        pen.write(f"Player_1: {score_1} Player_2: {score_2}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if ((ball.xcor() > 340) and (ball.xcor() < 350)) and ((ball.ycor() < paddle_2.ycor() +40 ) and (ball.ycor() > paddle_2.ycor() - 40)):
        ball.setx(340)
        ball.xspeed *= -1

    if ((ball.xcor() < -340) and (ball.xcor() > -350)) and ((ball.ycor() < paddle_1.ycor() +40 ) and (ball.ycor() > paddle_1.ycor() - 40)):
        ball.setx(-340)
        ball.xspeed *= -1