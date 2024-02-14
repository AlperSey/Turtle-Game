import turtle
import random

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("Turtle Game")

game_over = False
score = 0
FONT = ('Arial',20,'normal')
move_size = 10

# turtle list
turtle_list = []

# Score Table
score_table = turtle.Turtle()
def score_setup():

    score_table.hideturtle()
    score_table.penup()

    top_height = screen.window_height()
    y = top_height * 0.43

    score_table.goto(0,y)
    score_table.write("Score: 0",move=False,align='center', font=FONT)

# Time Table
time_table = turtle.Turtle()
def time_setup():
    time_table.hideturtle()
    time_table.penup()

    top_height = screen.window_height()
    y = top_height * 0.37

    time_table.goto(0, y)
    time_table.write("Time: 30", move=False, align='center', font=FONT)





def real_turtle(x,y):
    little_turtle = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_table.clear()
        score_table.write("Score: {}".format(score), move=False, align='center', font=FONT)
        #print(x,y)
    little_turtle.onclick(handle_click)

    little_turtle.penup()
    little_turtle.shape("turtle")
    little_turtle.shapesize(1.2,1.2)
    little_turtle.goto(x * move_size,y * move_size)
    turtle_list.append(little_turtle)






def turtle_coordinate():
    for x in range(-20,30,10):
        for y in range(-10,30,10):
            real_turtle(x,y)

def turtle_hides():
    for t in turtle_list:
        t.hideturtle()


def turtle_show():
    if not game_over:
        turtle_hides()
        random.choice(turtle_list).showturtle()
        screen.ontimer(turtle_show, 700)

def counter_time(time):
    global game_over
    time_table.clear()

    if time > 0:
        time_table.write("Time : {}".format(time), move=False, align='center', font=FONT)
        screen.ontimer(lambda: counter_time(time - 1), 1000)
    else:
        game_over = True
        time_table.clear()
        turtle_hides()
        time_table.write(arg="Game Over", move=False, align='center', font=FONT)



# All Functions
turtle.tracer(0)

score_setup()
turtle_coordinate()
time_setup()
turtle_hides()
turtle_show()
counter_time(10)

turtle.tracer(1)



turtle.mainloop()