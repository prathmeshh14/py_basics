import turtle as t
import random as r
import time as ti

delay = 0.1
score = 0
high_score = 0

bodies = []


s = t.Screen()
s.title("Snake Game")
s.bgcolor("grey")
s.setup(width=600, height=600)
s.tracer(0)


head = t.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = t.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0, 200)


sb = t.Turtle()
sb.speed(0)
sb.shape("square")
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write(
    "Score: 0   High Score: 0",
    align="center",
    font=("Arial", 18, "normal")
)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    if head.direction == "down":
        head.sety(y - 20)

    if head.direction == "left":
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(x + 20)


s.listen()
s.onkeypress(go_up, "Up")
s.onkeypress(go_down, "Down")
s.onkeypress(go_left, "Left")
s.onkeypress(go_right, "Right")


while True:
    s.update()

    # Wall collision
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        ti.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for body in bodies:
            body.goto(1000, 1000)

        bodies.clear()

        score = 0
        delay = 0.1

        sb.clear()
        sb.write(
            f"Score: {score}   High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal"),
        )


    if head.distance(food) < 20:
        x = r.randint(-14, 14) * 20
        y = r.randint(-14, 14) * 20
        food.goto(x, y)

        new_body = t.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("lightgreen")
        new_body.penup()
        bodies.append(new_body)

        delay -= 0.002

        score += 10
        if score > high_score:
            high_score = score

        sb.clear()
        sb.write(
            f"Score: {score}   High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal"),
        )


    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()


    for body in bodies:
        if body.distance(head) < 20:
            ti.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in bodies:
                segment.goto(1000, 1000)

            bodies.clear()

            score = 0
            delay = 0.1

            sb.clear()
            sb.write(
                f"Score: {score}   High Score: {high_score}",
                align="center",
                font=("Arial", 18, "normal"),
            )

    ti.sleep(delay)

s.mainloop()