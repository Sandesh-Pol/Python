from tkinter import *
import random

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPEED = 300

SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "#D66D75"
FOOD_COLOUR = "#FF0000"
BACKGROUND_COLOUR = "#000000"

class Food:
    def __init__(self):
        x = random.randint(0, GAME_WIDTH//SPACE_SIZE-1) * SPACE_SIZE
        y = random.randint(0, GAME_HEIGHT//SPACE_SIZE-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOUR)
            self.squares.append(square)

def next_turn(snake, food):
    x, y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOUR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 10
        label.config(text="Score : {}".format(score))
        canvas.delete("food")
        food = Food()

    else:
        x, y = snake.coordinates[-1]
        square = snake.squares[-1]
        canvas.delete(square)
        snake.coordinates.pop()
        snake.squares.pop()

    if check_collision(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_dir(new_direction):
    global direction
    direction = new_direction

def check_collision(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True
    for segment in snake.coordinates[1:]:
        if x == segment[0] and y == segment[1]:
            return True
    return False

def game_over():
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2, text="Game Over", fill="white", font=("Helvetica", 32), anchor="center")
    window.update()
    window.after(2000, window.destroy)

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score : {}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

next_turn(snake, food)

window.bind("<Up>", lambda event: change_dir("up"))
window.bind("<Down>", lambda event: change_dir("down"))
window.bind("<Left>", lambda event: change_dir("left"))
window.bind("<Right>", lambda event: change_dir("right"))

window.mainloop()
