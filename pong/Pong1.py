import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Mai")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0 PlayerB: 0", align="center", font=("Courier", 24, "bold"))

# functions
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)

def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
      wn.update()

      # move the ball
      ball.setx(ball.xcor() + ball.dx)
      ball.sety(ball.ycor() + ball.dy)

      # border checking
      if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay sound.wav&")

      if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay sound.wav&")

      if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

      if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

      # paddle and ball collisions 
      if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay sound.wav&")

      if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1 
        os.system("afplay sound.wav&")