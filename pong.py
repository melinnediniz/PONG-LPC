import random
import time
from functions import *

# defining constants
FONT = "Press Start 2P"
UP_DOWN_SOUND = "assets/bounce.wav"
SCORE_SOUND = "assets/score.wav"
BUTTON_SOUND = "assets/button.wav"
FPS = 1 / 60

# defining global variables
single_play = False
level = ''
ball_dx = 1
score_win = 5

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
        play_sound(BUTTON_SOUND)
        main_screen.clear()
        select_mode()
    elif -85 < x < 82 and -105 < y < -62:
        print('exit game')
        turtle.bye()


# calling the function
turtle.listen()
turtle.onscreenclick(button_actions, 1)


def select_mode():
    main_screen.bgcolor('black')
    draw_text(xcor=0, ycor=120, color="#F37746", msg="SELECT MODE", fontsize=36)

    draw_button(0, 0, '#17B119', 'MULTIPLAYER', 15)
    draw_button(0, -60, '#E5EB40', 'SINGLE PLAYER', 15)

    draw_text(0, -295, "red", "PRESS 'ESC' TO EXIT", 10)
    exit_game()

    def chosen_mode(x, y):
        global single_play
        if -115 < x < 110:
            if 10 < y < 30:
                print(x, y)
                print('Multiplayer')
                single_play = False
                print(f'npc joga? {single_play}')
                main_screen.clear()
                level_select()
            elif -50 < y < -35:
                print(x, y)
                print('Single player')
                single_play = True
                print(f'npc joga? {single_play}')
                main_screen.clear()
                level_select()

        play_sound(BUTTON_SOUND)

    main_screen.listen()
    main_screen.onscreenclick(chosen_mode, 1)


def level_select():
    main_screen.bgcolor('black')
    # draw game name in the top
    draw_text(xcor=0, ycor=120, color="#F37746", msg="CHOOSE LEVEL", fontsize=36)

    draw_button(0, 0, '#17B119', 'EASY', 20)
    draw_button(0, -60, '#E5EB40', 'MEDIUM', 20)
    draw_button(0, -120, '#FC7614', 'HARD', 20)

    draw_text(0, -295, "red", "PRESS 'ESC' TO EXIT", 10)
    exit_game()

    def chosen_level(x, y):
        global ball_dx, score_win, level
        if -100 < x < 85:
            if 10 < y < 45:
                print(x, y)
                print('Level 1')
                level = 'easy'
                ball_dx = 8
            elif -50 < y < -10:
                print(x, y)
                print('Level 2')
                level = 'medium'
                ball_dx = 16
            elif -110 < y < -80:
                print(x, y)
                print('Level 3')
                level = 'hard'
                ball_dx = 20
                score_win = 10
            play_sound(BUTTON_SOUND)
            main_screen.clear()
            play_game()

    main_screen.listen()
    main_screen.onscreenclick(chosen_level, 1)


def play_game():
    # exit game warning
    draw_text(-265, -295, "red", "PRESS 'ESC' TO EXIT", 10)
    exit_game()
    # pause warning
    draw_text(245, -295, "yellow", "PRESS 'SPACE' TO PAUSE", 10)

    print(level)

    global PAUSED
    PAUSED = False

    # draw window
    game_screen = turtle.Screen()
    game_screen.title("PLAYING PING PONG")
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
    win.color("green")
    win.penup()
    win.hideturtle()
    win.goto(0, 0)

    actions = dict(
        up_1=lambda: move_up(paddle_1, is_paused=PAUSED),
        down_1=lambda: move_down(paddle_1, is_paused=PAUSED),
        up_2=lambda: move_up(paddle_2, is_paused=PAUSED),
        down_2=lambda: move_down(paddle_2, is_paused=PAUSED),
    )

    pause_text = turtle.Turtle()
    pause_text.hideturtle()

    def pause():
        global PAUSED
        if not PAUSED:
            pause_text.shape('square')
            pause_text.color('red')
            pause_text.goto(0, 0)
            pause_text.write("PAUSED", align='center', font=(FONT, 24, "normal"))
            pause_text.penup()
            PAUSED = True
        else:
            pause_text.clear()
            PAUSED = False

    def reset():
        global score_win
        game_screen.clear()
        ball.dx = 0
        ball.dy = 0
        select_mode()
        if level == 'hard':
            score_win = 5
        select_mode()

    # keyboard
    keys_pressed = set()
    game_screen.listen()
    if score_1 == score_win or score_2 == score_win:
        game_screen.onkeypress(reset, 'r')
    
    game_screen.onkeypress(pause, 'space')
    game_screen.onkeypress(lambda: keys_pressed.add('up_1'), 'w')
    game_screen.onkeypress(lambda: keys_pressed.add('down_1'), "s")
    game_screen.onkeyrelease(lambda: keys_pressed.remove('up_1'), 'w')
    game_screen.onkeyrelease(lambda: keys_pressed.remove('down_1'), "s")

    if not single_play:
        game_screen.onkeypress(lambda: keys_pressed.add('up_2'), "Up")
        game_screen.onkeypress(lambda: keys_pressed.add('down_2'), "Down")
        game_screen.onkeyrelease(lambda: keys_pressed.remove('up_2'), "Up")
        game_screen.onkeyrelease(lambda: keys_pressed.remove('down_2'), "Down")

    def listen_keypress():
        for action in keys_pressed:
            actions[action]()
        game_screen.ontimer(listen_keypress, 1000 // 30)

    listen_keypress()

    while True:
        time.sleep(FPS)
        game_screen.update()

        if not PAUSED:
            # ball move
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # check mode game
            if single_play:
                npc(ball, paddle_2, level)

        # collision with top wall
        if ball.ycor() > 285:
            ball.sety(285)
            ball.dy *= -1
            play_sound(UP_DOWN_SOUND)

        # collision with down wall
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.dy *= -1
            play_sound(UP_DOWN_SOUND)

        # collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            if score_1 == score_win or score_2 == score_win:
                play_sound('assets/wining.wav')
            else:
                play_sound(SCORE_SOUND)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = -ball_dx / 2
            ball.dy = -0.4

        # collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            hud.clear()
            hud.write("{} : {}".format(score_1, score_2), align="center", font=(FONT, 24, "normal"))
            if score_1 == score_win or score_2 == score_win:
                play_sound('assets/wining.wav')
            else:
                play_sound(SCORE_SOUND)
            ball.goto(0, random.randint(-200, 200))
            ball.dx = ball_dx / 2
            ball.dy = -0.4

        # collision with paddle 1
        if ball.xcor() < -330 and paddle_1.ycor() + 55 > ball.ycor() > paddle_1.ycor() - 55:
            ball.dx = ball_dx * 2
            play_sound(UP_DOWN_SOUND)

            # part upper
            if paddle_1.ycor() + 55 > ball.ycor() > paddle_1.ycor() + 15:
                ball.dy = 10
            # part bottom
            elif paddle_1.ycor() - 15 > ball.ycor() > paddle_1.ycor() - 55:
                ball.dy = -10
            # part middle
            else:
                ball.dy = random.uniform(-3, 3)

        # collision with paddle 2
        if ball.xcor() > 330 and paddle_2.ycor() + 55 > ball.ycor() > paddle_2.ycor() - 55:
            ball.dx = -ball_dx * 2
            play_sound(UP_DOWN_SOUND)

            # part upper
            if paddle_2.ycor() + 55 >= ball.ycor() >= paddle_2.ycor() + 15:
                ball.dy = 10
            # part bottom
            elif paddle_2.ycor() - 15 >= ball.ycor() >= paddle_2.ycor() - 55:
                ball.dy = -10
            # part middle
            else:
                ball.dy = random.uniform(-3, 3)

        # win condition
        if score_1 == score_win or score_2 == score_win:
            winner = "1P" if score_1 > score_2 else "2P"
            win.write("CONGRATS, {} YOU'RE THE WINNER!".format(winner), align="center",
                      font=(FONT, 18, "normal"))
            draw_text(0, -100, 'gray', "PRESS 'R' TO RESET", 15)
            turtle.done()


if __name__ == '__main__':
    start_page()
    turtle.done()
