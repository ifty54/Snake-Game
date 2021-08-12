# Snake-Game
traditional snake game using python3

import turtle
import time
import random

delay = 0.1

#score
score = 0
High_score = 0

wn = turtle.Screen()
wn.title("my game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

#head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score: 0 High score: 0", align="center", font=("Courier", 24, "normal"))

#func
def go_up():
    if head.direction != "down":
      head.direction = "up"

def go_down():
    if head.direction != "down":
      head.direction = "down"

def go_left():
    if head.direction != "right":
      head.direction = "left"

def go_right():
    if head.direction != "left":
      head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#main gaming loop
while True:
    wn.update()

    #check for collision to the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() < -290 or head.ycor() > 290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

#check collision with the food to head

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add new segmnt
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #decrese delay
        delay -=0.001

        #increase score
        score += 10

        if score > High_score:
            High_score = score

        pen.clear()
        pen.write("score: {}  High score: {}".format(score, High_score), align="center", font=("Courier", 24, "normal")),

# move the end segmnts first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

#move segmnt 0 where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    
    #check for head collision with its body
    for segment in segments:
       if segment.distance(head) < 20:
           time.sleep(1)
           head.goto(0,0)
           head.direction = "stop"

#hide the segments
           for segment in segments:
               segment.goto(1000,1000)

#clear the segments list
           segments.clear()

           score = 0

    time.sleep(delay)

wn.mainloop()

