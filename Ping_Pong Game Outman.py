# Ping_Pong Game Outman

#import trutle Module

import turtle

wind = turtle.Screen() #intialise screen 
wind.title("Ping_Pong Outman") #set the title of window
wind.bgcolor("Purple")  #set the color of the background
wind.setup(width=800, height=600)  #the dimensions of the window
wind.tracer(0)  #stop window from refraiching automatically

#welcoming phase
welcome = turtle.Turtle()
welcome.goto(0,-270)
welcome.color("white")
welcome.penup()
welcome.hideturtle()
welcome.write(" welcome in my game!! I hope you enjoy it :) " , align="center", font=("Arial",9,"normal"))


#madarb1
madrab1 = turtle.Turtle()
madrab1.speed(0)   #the speed of animation of madrab1
madrab1.shape("square")
madrab1.color("yellow")
madrab1.shapesize(stretch_len=1, stretch_wid=5)
madrab1.penup()  #stops drawing lines
madrab1.goto(-370,0)  #positions of the ball(x,y)
#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("white")
madrab2.shapesize(stretch_len=1, stretch_wid=5)
madrab2.penup()
madrab2.goto(370,0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 2.5
ball.dy = 2.5

#score
score1 = 0
score2= 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0   Player 2: 0", align="center", font=("Arial",24,"normal"))


#functions
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


#Keyboardbininds
wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")


#main game loop

while True:
    wind.update()  #updates the screen every time the loop run

     #move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <-290:
       ball.sety(-290)
       ball.dy *= -1  
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Arial",24,"normal"))

    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Arial",24,"normal"))


   #tsadom madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < madrab2.ycor() + 40)):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < madrab1.ycor() + 40)):
        ball.setx(-340)
        ball.dx *= -1
