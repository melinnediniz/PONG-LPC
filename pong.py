from tkinter import mainloop
import turtle
import winsound
import random

# defining constants
FONT = "Press Start 2P"
UP_DOWN_SOUND = "assets/bounce.wav"
SCORE_SOUND = "assets/258020__kodack__arcade-bleep-sound.wav"

start_pg = turtle.Screen()
start_pg.bgcolor('black')
start_pg.setup(width=800, height=600)


# draw first window
def start_page():
    
    # draw game name in the top
    game_name = turtle.Turtle()
    game_name.speed(0)
    game_name.hideturtle()
    game_name.penup()
    game_name.color("white")
    game_name.goto(0, 160)
    game_name.write('PING PONG', align="center", font=(FONT, 50, 'normal'))

    # draw start button
    start_button = turtle.Turtle()
    start_button.speed(0)
    start_button.hideturtle()
    start_button.pensize(4)
    start_button.color('#BFDEB4')
    start_button.penup()
    start_button.goto(-112, -20)

    # draw button borders
    start_button.fillcolor('#0A1B08')
    start_button.begin_fill()
    for _ in range(2):
        start_button.pendown()
        start_button.forward(220)
        start_button.left(90)
        start_button.forward(70)
        start_button.left(90)
    start_button.end_fill()
    
    start_button.penup()
    start_button.goto(0, 0)
    start_button.write('Start Game', align='center', font=(FONT, 15, 'normal'))

    exit_button = turtle.Turtle()
    exit_button.speed(0)
    exit_button.hideturtle()
    exit_button.pensize(4)
    exit_button.color('red')
    exit_button.penup()
    exit_button.goto(0, -100)
    exit_button.write('Exit Game', align='center', font=(FONT, 15, 'normal'))


# function to start or exit game
def button_actions(x, y):
    global start_pg
    if -110 < x < 100 and 0 < y < 40:
        print('Start Game')
        # winsound.PlaySound('assets/wining.wav', winsound.SND_ASYNC)
        start_pg.clear()
        main()
    elif -85 < x < 82 and -105 < y < -62:
        print('exit game')
        turtle.bye()


# calling the function
turtle.listen()
turtle.onscreenclick(button_actions, 1)


def main():

    # draw window    
    screen = turtle.Screen()
    screen.title("My Pong")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    screen.bgpic('assets/game_background.png')
    
    # scores
    score_1 = 0
    score_2 = 0
    score_win = 10

    # draw paddle 1
    paddle_1 = turtle.Turtle()
    paddle_1.speed(0)
    paddle_1.shape("square")
    paddle_1.color("#CD7011")
    paddle_1.shapesize(stretch_wid=5, stretch_len=1)
    paddle_1.penup()
    paddle_1.goto(-350, 0)

    # draw paddle 2
    paddle_2 = turtle.Turtle()
    paddle_2.speed(0)
    paddle_2.shape("square")
    paddle_2.color("#16899E")
    paddle_2.shapesize(stretch_wid=5, stretch_len=1)
    paddle_2.penup()
    paddle_2.goto(350, 0)

    # draw ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("#8BD580")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.15
    ball.dy = 0

    # score head-up display
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(0, 250)
    hud.write("0 : 0", align="center", font=(FONT, 24, "normal"))
    
    # draw win screen
    win = turtle.Turtle()
    win.speed(0)
    win.shape("square")
    win.color("white")
    win.penup()
    win.hideturtle()
    win.goto(0, 0)

    # draw exit warning
    exit_warning = turtle.Turtle()
    exit_warning.speed(0)
    exit_warning.hideturtle()
    exit_warning.color("red")
    exit_warning.penup()
    exit_warning.goto(0, -295)
    exit_warning.write("PRESS 'SPACE' TO EXIT", align="center", font=("Small Fonts", 12, "normal"))

    # move paddle up
    def move_up(paddle):
        y = paddle.ycor()
        if y < 250:
            y += 20
        else:
            y = 250
        paddle.sety(y)

    # move paddle down
    def move_down(paddle):
        y = paddle.ycor()
        if y > -250:
            y += -20
        else:
            y = -250
        paddle.sety(y)

    # paddles movement
    def paddle_1_up():
        move_up(paddle_1)

    def paddle_1_down():
        move_down(paddle_1)

    def paddle_2_up():
        move_up(paddle_2)

    def paddle_2_down():
        move_down(paddle_2)

    def exit_game():
        turtle.clear()
        turtle.bye()

    # mapping keys
    screen.listen()
    screen.onkeypress(paddle_1_up, "w")
    screen.onkeypress(paddle_1_down, "s")
    screen.onkeypress(paddle_2_up, "Up")
    screen.onkeypress(paddle_2_down, "Down")
    screen.onkeypress(exit_game, "space")

    while True:
        screen.update()

        # ball move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with top wall
        if ball.ycor() > 285:
            ball.sety(285)
            ball.dy *= -1
            winsound.PlaySound(UP_DOWN_SOUND,  winsound.SND_ASYNC)

        # collision with down wall
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            winsound.PlaySound(UP_DOWN_SOUND,  winsound.SND_ASYNC)

        # collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            winsound.PlaySound(SCORE_SOUND,  winsound.SND_ASYNC)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = 0.40

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            winsound.PlaySound(SCORE_SOUND, winsound.SND_ASYNC)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = -0.40

        # collision with paddle 1
        if ball.xcor() < -330 and paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50:
            ball.dx = 0.30
            winsound.PlaySound(UP_DOWN_SOUND,  winsound.SND_ASYNC)

            # part upper
            if paddle_1.ycor()+55 > ball.ycor() > paddle_1.ycor()+15:
                ball.dy = 0.1
            # part bottom
            elif paddle_1.ycor()-15 > ball.ycor() > paddle_1.ycor()-55:
                ball.dy = -0.1
            # part middle
            else: 
                ball.dy = random.uniform(-0.05,0.05)

        # collision with paddle 2
        if ball.xcor() > 330 and paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50:
            ball.dx = -0.30
            winsound.PlaySound(UP_DOWN_SOUND,  winsound.SND_ASYNC)

            # part upper
            if paddle_2.ycor()+55 >= ball.ycor() >= paddle_2.ycor()+15:
                ball.dy = 0.1
            # part bottom
            elif paddle_2.ycor()-15 >= ball.ycor() >= paddle_2.ycor()-55:
                ball.dy = -0.1
            # part middle
            else: 
                ball.dy = random.uniform(-0.05,0.05)
        
        # win condition
        if score_1 == score_win or score_2 == score_win:
            winner = "1P" if score_1 > score_2 else "2P"
            score_1 = score_2 = 0
            win.write("Congrats, {} you're the winner!".format(winner), align="center", font=("Press Start 2P",
                                                                                              24, "normal"))


if __name__ == '__main__':

    start_page()
    mainloop()
