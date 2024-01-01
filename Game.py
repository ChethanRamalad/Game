from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "Right"

    def move(self):
        head = self.body[0].copy()

        if self.direction == "Right":
            head[0] += SPACE_SIZE
        elif self.direction == "Left":
            head[0] -= SPACE_SIZE
        elif self.direction == "Up":
            head[1] -= SPACE_SIZE
        elif self.direction == "Down":
            head[1] += SPACE_SIZE

        self.body.insert(0, head)

    def check_collision(self):
        if (
            self.body[0][0] < 0
            or self.body[0][1] < 0
            or self.body[0][0] >= GAME_WIDTH
            or self.body[0][1] >= GAME_HEIGHT
        ):
            return True

        for segment in self.body[1:]:
            if segment == self.body[0]:
                return True

        return False

    def increase_length(self):
        self.body.append([-1, -1])

    def draw(self, canvas):
        for segment in self.body:
            canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + SPACE_SIZE,
                segment[1] + SPACE_SIZE,
                fill=SNAKE_COLOR,
            )

class Food:
    def __init__(self):
        self.position = [0, 0]
        self.spawn_food()

    def spawn_food(self):
        x = random.randint(0, (GAME_WIDTH - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
        self.position = [x, y]

    def draw(self, canvas):
        canvas.create_rectangle(
            self.position[0],
            self.position[1],
            self.position[0] + SPACE_SIZE,
            self.position[1] + SPACE_SIZE,
            fill=FOOD_COLOR,
        )

def next_turn():
    snake.move()
    if snake.check_collision():
        game_over()
        return

    if snake.body[0] == food.position:
        snake.increase_length()
        food.spawn_food()

    canvas.delete("all")
    snake.draw(canvas)
    food.draw(canvas)

    window.after(SPEED, next_turn)

def changedirection(event):
    if event.keysym == "Right" and snake.direction != "Left":
        snake.direction = "Right"
    elif event.keysym == "Left" and snake.direction != "Right":
        snake.direction = "Left"
    elif event.keysym == "Up" and snake.direction != "Down":
        snake.direction = "Up"
    elif event.keysym == "Down" and snake.direction != "Up":
        snake.direction = "Down"

def game_over():
    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2,
        text="Game Over",
        font=("Helvetica", 30),
        fill="white",
    )
    window.unbind("<Up>")
    window.unbind("<Down>")
    window.unbind("<Left>")
    window.unbind("<Right>")

window = Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()

snake = Snake()
food = Food()

window.bind("<Up>", changedirection)
window.bind("<Down>", changedirection)
window.bind("<Left>", changedirection)
window.bind("<Right>", changedirection)

next_turn()

window.mainloop()
