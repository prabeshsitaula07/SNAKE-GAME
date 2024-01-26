import turtle
import time
import random

delay = 0.1


#score
score=0
high_score=0


wn = turtle.Screen()
wn.title("Snake Game by SJAN")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # turn off the screen update

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "right"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0",align="center",font =("Courier",24,"normal"))

# Functions
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

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main loop
while True:
    wn.update()

        # Check for collision with border
    if (
        head.xcor() > 299
        or head.xcor() < -299
        or head.ycor() > 299
        or head.ycor() < -299
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Reset the score to 0
        score = 0

        # Update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        # Move the food using the random module
        x = random.randint(-299, 299)
        y = random.randint(-299, 299)
        food.goto(x, y)

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        
        #increase the score
        score+=10
        if score >high_score:
            high_score=score
        pen.clear()    
            
        pen.write("score:{} High score {} ".format(score,high_score),align="center")    

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the segments to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check the head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

    time.sleep(delay)
