# Christian Thompsons tutorial på YouTube
# Kodeklubben Salangen

import turtle
import os # For lyd på Mac og Linux
# import winsound # For lyd på Windows

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Poeng
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Poengtavle
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("arial", 24, "normal"))

# Funksjoner
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


# Tastebindinger
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main loop
while True:
	wn.update()

	# Beveg ballen
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Grensesjekk
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		# Mac-lyd: afplay, linux: aplay
		# winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # For Windows
		os.system("afplay pong.wav&") # & spiller lyden asynkront

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		# Mac-lyd: afplay, linux: aplay
		# winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # For Windows
		os.system("afplay pong.wav&") # & spiller lyden asynkront

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("arial", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("arial", 24, "normal"))

	# Kolisjoner
	if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
		ball.setx(340)
		ball.dx *= -1
		# Mac-lyd: afplay, linux: aplay
		# winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # For Windows
		os.system("afplay pong.wav&") # & spiller lyden asynkront


	if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
		ball.setx(-340)
		ball.dx *= -1
		# Mac-lyd: afplay, linux: aplay
		# winsound.PlaySound("pong.wav", winsound.SND_ASYNC) # For Windows
		os.system("afplay pong.wav&") # & spiller lyden asynkront