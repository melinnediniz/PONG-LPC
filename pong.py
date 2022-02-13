import random
import time
from functions import *

# defining constants
FONT = "Press Start 2P"
UP_DOWN_SOUND = "assets/bounce.wav"
SCORE_SOUND = "assets/341695__projectsu012__coins-1.wav"
FPS = 1 / 60

# defining global variables
level = 1
paddle_width = 5
paddle_collision = 50
ball_dx = 2
score_win = 3

# draw main screen
main_screen = turtle.Screen()
main_screen.bgcolor('black')
main_screen.title("PING PONG")
main_screen.setup(width=800, height=600)
main_screen.tracer(0)


# draw first window
def start_page():
    # draw game name on the top
    draw_text(xcor=0, ycor=120, color="#F37746", msg="PING PONG", fontsize=50)

    # draw button borders
    start_button = turtle.Turtle()
    start_button.goto(-112, -20)
    start_button.fillcolor('#0A1B08')
    start_button.begin_fill()
    for _ in range(2):
        start_button.pendown()
        start_button.forward(220)
        start_button.left(90)
        start_button.forward(70)
        start_button.left(90)
    start_button.end_fill()

    draw_button(xcor=0, ycor=0, color='#BFDEB4', msg='Start Game', fontsize=15)
    draw_button(xcor=0, ycor=-100, color='red', msg='Exit Game', fontsize=15)


# function to start or exit game
def button_actions(x, y):
    global main_screen
    if -110 < x < 100 and 0 < y < 40:
        print('Start Game')
        play_sound('assets/403016__inspectorj__ui-confirmation-alert-c1.wav')
        main_screen.clear()
        level_select()
    elif -85 < x < 82 and -105 < y < -62:
        print('exit game')
        turtle.bye()


# calling the function
turtle.listen()
turtle.onscreenclick(button_actions, 1)


def level_select():
    main_screen.bgcolor('black')
    # draw game name in the top
    draw_text(xcor=0, ycor=120, color="#F37746", msg="CHOOSE LEVEL", fontsize=36)

    draw_button(0, 0, '#17B119', 'EASY', 20)
    draw_button(0, -60, '#E5EB40', 'MEDIUM', 20)
    draw_button(0, -120, '#FC7614', 'HARD', 20)

    draw_text(0, -295, "red", "PRESS 'SPACE' TO EXIT", 10)
    exit_game()

    def level_choosed(x, y):
        global ball_dx, paddle_width, score_win
        if -100 < x < 85:
            if 10 < y < 45:
                print(x, y)
                print('Level 1')
                ball_dx = 1.5
            elif -50 < y < -10:
                print(x, y)
                print('Level 2')
                ball_dx = 2
            elif -110 < y < -80:
                print(x, y)
                print('Level 3')
                ball_dx = 2.5
                paddle_width = 3.5
                score_win = 15
            play_sound('assets/403016__inspectorj__ui-confirmation-alert-c1.wav')
            main_screen.clear()
            play_game()

    main_screen.listen()
    main_screen.onscreenclick(level_choosed, 1)

def play_game():
    # exit game warning
    draw_text(0, -295, "red", "PRESS 'SPACE' TO EXIT", 10)
    exit_game()

    # draw window
    game_screen = turtle.Screen()
    game_screen.title("My Pong")
    game_screen.bgcolor("black")
    game_screen.setup(width=800, height=600)
    game_screen.tracer(0)
    game_screen.bgpic('assets/game_background.png')

    # scores
    score_1 = 0
    score_2 = 0

    # draw paddle 1
    paddle_1 = turtle.Turtle()
    paddle_1.speed(0)
    paddle_1.shape("square")
    paddle_1.color("#CD7011")
    paddle_1.shapesize(stretch_wid=paddle_width, stretch_len=1)
    paddle_1.penup()
    paddle_1.goto(-350, 0)

    # draw paddle 2
    paddle_2 = turtle.Turtle()
    paddle_2.speed(0)
    paddle_2.shape("square")
    paddle_2.color("#16899E")
    paddle_2.shapesize(stretch_wid=paddle_width, stretch_len=1)
    paddle_2.penup()
    paddle_2.goto(350, 0)

    # draw ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("#8BD580")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = ball_dx
    ball.dy = 0

    # score head-up display
    draw_text(xcor=-140, ycor=255, color='#CD7011', msg='1P', fontsize=20)
    draw_text(xcor=160, ycor=255, color='#16899E', msg='2P', fontsize=20)
    hud = turtle.Turtle()
    hud.speed(0)
    hud.shape("square")
    hud.color("white")
    hud.penup()
    hud.hideturtle()
    hud.goto(6, 250)
    hud.write("0 : 0", align="center", font=(FONT, 24, "normal"))

    # draw win screen
    win = turtle.Turtle()
    win.speed(0)
    win.shape("square")
    win.color("white")
    win.penup()
    win.hideturtle()
    win.goto(0, 0)

    actions = dict(
        up_1=lambda: move_up(paddle_1),
        down_1=lambda: move_down(paddle_1),
        up_2=lambda: move_up(paddle_2),
        down_2=lambda: move_down(paddle_2),
    )

    # keyboard
    keys_pressed = set()
    game_screen.listen()
    game_screen.onkeypress(lambda: keys_pressed.add('up_1'), 'w')
    game_screen.onkeypress(lambda: keys_pressed.add('down_1'), "s")
    game_screen.onkeypress(lambda: keys_pressed.add('up_2'), "Up")
    game_screen.onkeypress(lambda: keys_pressed.add('down_2'), "Down")

    game_screen.onkeyrelease(lambda: keys_pressed.remove('up_1'), 'w')
    game_screen.onkeyrelease(lambda: keys_pressed.remove('down_1'), "s")
    game_screen.onkeyrelease(lambda: keys_pressed.remove('up_2'), "Up")
    game_screen.onkeyrelease(lambda: keys_pressed.remove('down_2'), "Down")

    def listen_keypress():
        for action in keys_pressed:
            actions[action]()
        game_screen.ontimer(listen_keypress, 1000 // 30)

    listen_keypress()

    while True:
        game_screen.update()

        # ball move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # collision with top wall
        if ball.ycor() > 285:
            ball.sety(285)
            ball.dy *= -1
            winsound.PlaySound(UP_DOWN_SOUND, winsound.SND_ASYNC)

        # collision with down wall
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            winsound.PlaySound(UP_DOWN_SOUND, winsound.SND_ASYNC)

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            play_sound(SCORE_SOUND)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = -ball_dx
            ball.dy = -0.4

        # collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            play_sound(SCORE_SOUND)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = ball_dx
            ball.dy = -0.4

        # collision with paddle 1
        if ball.xcor() < -330 and paddle_1.ycor() + 55 > ball.ycor() > paddle_1.ycor() - 55:
            ball.dx = ball_dx
            play_sound(UP_DOWN_SOUND)

            # part upper
            if paddle_1.ycor() + 55 > ball.ycor() > paddle_1.ycor() + 15:
                ball.dy = 0.5
            # part bottom
            elif paddle_1.ycor() - 15 > ball.ycor() > paddle_1.ycor() - 55:
                ball.dy = -0.5
            # part middle
            else:
                ball.dy = random.uniform(-0.05, 0.05)

        # collision with paddle 2
        if ball.xcor() > 330 and paddle_2.ycor() + 55 > ball.ycor() > paddle_2.ycor() - 55:
            ball.dx = -ball_dx
            play_sound(UP_DOWN_SOUND)

            # part upper
            if paddle_2.ycor() + 55 >= ball.ycor() >= paddle_2.ycor() + 15:
                ball.dy = 0.5
            # part bottom
            elif paddle_2.ycor() - 15 >= ball.ycor() >= paddle_2.ycor() - 55:
                ball.dy = -0.5
            # part middle
            else:
                ball.dy = random.uniform(-0.05, 0.0)

        # win condition
        if score_1 == score_win or score_2 == score_win:
            winner = "1P" if score_1 > score_2 else "2P"
            score_1 = score_2 = 0
            play_sound("assets/wining.wav")
            win.write("Congrats, {} you're the winner!".format(winner), align="center",
                      font=(FONT, 15, "normal"))


if __name__ == '__main__':
    start_page()
    time.sleep(FPS)
    turtle.done()
