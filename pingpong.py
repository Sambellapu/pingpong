from turtle import *
padle1 = Turtle()
padle2 = Turtle()
ball = Turtle()
pen = Turtle()
win = Turtle()
root = Screen()
root.setup(width=300,height=200)
win.goto(0,140)
score1 = 0
score2 = 0

def up():
    padle1.sety(padle1.ycor() + 20)


def down():
    padle1.sety(padle1.ycor() - 20)


def up2():
    padle2.sety(padle2.ycor() + 20)


def down2():
    padle2.sety(padle2.ycor() - 20)


root.bgcolor("black")
root.tracer(0)
root.update()
padle1.speed(0)
padle1.shape("square")
padle1.color("white")
padle1.shapesize(6,1)
padle1.up()
padle1.goto(-285,0)

padle2.speed(0)
padle2.shape("square")
padle2.color("white")
padle2.shapesize(6,1)
padle2.up()
padle2.goto(285,0)

ball.shape("circle")
ball.color("white")
ball.up()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2
ball.speed(10)

pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,180)
pen.write("Player 1:0            Player 2:0",align = "center",font = ("Arial",16))

win.hideturtle()
win.color("white")

while True:
    root.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.xcor() > 320:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score1 += 1
        pen.clear()
        pen.write(f"Player 1:{score1}            Player 2:{score2}",align = "center",font = ("Arial",16))

    if score1 == 20:
        win.write("Player 1 Wins",align = "center",font = ("Arial",16))
        break

    if score2 == 20:
        win.write("Player 2 Wins",align = "center",font = ("Arial",16))
        break

    if ball.xcor() < -320:
        ball.goto(0,0)
        ball.dx = ball.dx * -1
        score2 += 1
        pen.clear()
        pen.write(f"Player 1:{score1}            Player 2:{score2}",align = "center",font = ("Arial",16))

    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy *= -1

    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy *= -1

    if -295 < ball.xcor() < -285 and padle1.ycor() - 50 < ball.ycor() < padle1.ycor() + 50:
        ball.setx(-285)
        ball.dx *= -1

    if 285 < ball.xcor() < 295 and padle2.ycor() - 50 < ball.ycor() < padle2.ycor() + 50:
        ball.setx(285)
        ball.dx *= -1
    root.onkey(up,"Up")
    root.onkey(down,"Down")

    root.onkey(up2,"w")
    root.onkey(down2,"s")
    root.listen()
root.mainloop()