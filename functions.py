import winsound
import turtle
from pong import FONT, start_page, main_screen


# play sound function
def play_sound(sound_name):
    winsound.PlaySound(sound_name, winsound.SND_ASYNC)


# function to create a generic button
def draw_button(xcor, ycor, color, msg, fontsize):
    button = turtle.Turtle()
    button.speed(0)
    button.hideturtle()
    button.color(color)
    button.penup()
    button.goto(xcor, ycor)
    button.write(msg, align='center', font=(FONT, fontsize, 'normal'))


def draw_text(xcor, ycor, color, msg, fontsize):
    text = turtle.Turtle()
    text.speed(0)
    text.hideturtle()
    text.color(color)
    text.penup()
    text.goto(xcor, ycor)
    text.write(msg, align="center", font=(FONT, fontsize, "normal"))


# move paddle up
def move_up(paddle, single_play=False, nivel=''):
    y = paddle.ycor()
    if y < 250:
        if single_play:
                if nivel == 'easy':
                    y += 10
                if nivel == 'medium':
                    y += 15
                if nivel == 'hard':
                    y += 15
        else:
            y += 50
    else:
        y = 250
    paddle.sety(y)


# move paddle down
def move_down(paddle, single_play=False, nivel=''):
    y = paddle.ycor()
    if y > -250:
        if single_play:
            if nivel == 'easy':
                y += -10
            if nivel == 'medium':
                y += -15
            if nivel == 'hard':
                y += -15
        else:
            y += -50
    else:
        y = -250
    paddle.sety(y)


def exit_game():
    # draw exit warning
    turtle.onkeypress(turtle.bye, "space")


def reset_game():
    # draw_text(xcor=0, ycor=-200, color='blue', msg="PRESS 'R' TO RESET", fontsize=15)
    main_screen.clear()
    start_page()


