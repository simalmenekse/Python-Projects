print("GFG")
import random
import turtle as tr
from turtle import Turtle
import time

MOVE_DIST = 70
MOVE_DIST_1 = 10
COLOR_LIST = ['light blue', 'royal blue',
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue',
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink',
              'medium sea green', 'khaki']

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

FONT = ('arial', 18, 'normal')

import time
from turtle import Turtle
import random

FONT2 = ("Courier", 52, "normal")
FONT3 = ("Courier", 32, "normal")
ALIGNMENT = "center"
COLOR = "white"


try:
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    score = open('highestScore.txt', 'w').write(str(0))
except ValueError:
    score = 0

class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highScore = score
        self.goto(x=-580, y=260)
        self.lives = lives
        self.score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} \
        | Lives: {self.lives}", align='left', font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open('highestScore.txt', "w").write(str(self.highScore))

class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write("Breakout", align=ALIGNMENT, font=FONT2)
        self.goto(x=0, y=-180)
        self.write("Press Space to PAUSE or RESUME the Game",
                   align=ALIGNMENT,font=("Calibri", 14,"normal"))

    def change_color(self):
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def paused_status(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self, win):
        self.clear()
        if win == True:
            self.write("You Cleared the Game!", align=ALIGNMENT, font=FONT2)
        else:
            self.write("Game is Over!", align=ALIGNMENT, font=FONT2)

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("steel blue")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-280)

    def move_left(self):
        self.backward(MOVE_DIST)
    def move_right(self):
        self.forward(MOVE_DIST)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move_dist = MOVE_DIST_1
        self.y_move_dist = MOVE_DIST_1
        self.reset()

    def move(self):

        new_y = self.ycor() + self.y_move_dist
        new_x = self.xcor() + self.x_move_dist
        self.goto(x=new_x, y=new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move_dist *= -1
        if y_bounce:
            self.y_move_dist *= -1
    def reset(self):
        self.goto(x=0, y=-240)
        self.y_move_dist = 10

class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)

        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15

class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-570, 570, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)
    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)


screen = tr.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ui = UI()
ui.header()
score = Scoreboard(lives=5)
paddle = Paddle()
ball = Ball()
bricks = Bricks()

playing_game = True
game_paused = False

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
screen.onkey(key="space", fun=pause_game)

def check_collision_with_walls():
    global ball, score, playing_game, ui

    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        return
    if ball.ycor() < -280:
        ball.reset()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
        ui.change_color()
        return
def check_collision_with_paddle():
    global ball, paddle

    paddle_x = paddle.xcor()
    ball_x = ball.xcor()

    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return

def check_collision_with_bricks():
    global ball, bricks
    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000,3000)
                bricks.bricks.remove(brick)
            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)
            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

while playing_game:
    if not game_paused:
        screen.update()
        time.sleep(0.01)
        ball.move()

        check_collision_with_walls()
        check_collision_with_paddle()
        check_collision_with_bricks()

        if len(bricks.bricks) == 0:
            ui.game_over(win=True)
            break
        else:
            ui.paused_status()

tr.mainloop()