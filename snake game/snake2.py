import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0
bodies = []

# Creating screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)

# Creating head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating a food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.fillcolor("red")
food.penup()
food.ht()
food.goto(150, 200)
food.st()

# Creating a Score board
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0   |   Highest Score: 0")

# Creating function for moving
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Main loop
while True:
    s.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        head.goto(0, 0)
        head.direction = "stop"
        for body in bodies:
            body.ht()
        bodies.clear()
        score = 0
        delay = 0.1
        sb.clear()
        sb.write("Score: {}   |   Highest Score: {}".format(score, high_score))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the body snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)

        score += 100
        delay -= 0.001

        if score > high_score:
            high_score = score
        sb.clear()
        sb.write("Score: {}   |   Highest Score: {}".format(score, high_score))

    # Move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # Check collision for snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {}   |   Highest Score: {}".format(score, high_score))

    time.sleep(delay)

s.mainloop()
