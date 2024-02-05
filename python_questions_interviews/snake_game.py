import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")

        self.width = 600
        self.height = 400

        self.canvas = tk.Canvas(self.window, bg='black', width=self.width, height=self.height)
        self.canvas.pack()

        # Set up game variables
        self.cell_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.snake_dir = "Right"
        self.food = self.place_food()
        self.game_over = False

        # Draw initial snake and food
        self.draw_snake()
        self.draw_food()

        # Set up keyboard bindings
        self.window.bind("<Left>", self.go_left)
        self.window.bind("<Right>", self.go_right)
        self.window.bind("<Up>", self.go_up)
        self.window.bind("<Down>", self.go_down)

        # Start moving the snake
        self.move_snake()

        self.window.mainloop()

    def draw_snake(self):
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='green')

    def draw_food(self):
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='red')

    def place_food(self):
        return (random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size,
                random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size)

    def move_snake(self):
        if self.game_over:
            return

        head_x, head_y = self.snake[0]
        if self.snake_dir == "Left":
            head_x -= self.cell_size
        elif self.snake_dir == "Right":
            head_x += self.cell_size
        elif self.snake_dir == "Up":
            head_y -= self.cell_size
        elif self.snake_dir == "Down":
            head_y += self.cell_size

        new_head = (head_x, head_y)

        # Check for game over conditions
        if (head_x < 0 or head_x >= self.width or
                head_y < 0 or head_y >= self.height or
                new_head in self.snake):
            self.game_over = True
            self.canvas.create_text(self.width // 2, self.height // 2, text="Game Over", fill="white", font=("", 40))
            return

        # Move the snake
        self.snake = [new_head] + self.snake[:-1]

        # Check for snake eating food
        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.place_food()
            self.canvas.delete("all")
            self.draw_snake()
            self.draw_food()
        else:
            self.canvas.delete("all")
            self.draw_snake()
            self.draw_food()

        # Continue moving
        self.window.after(100, self.move_snake)

    def change_direction(self, new_dir):
        """Change snake direction without reversing."""
        opposite_dirs = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
        if self.snake_dir != opposite_dirs.get(new_dir):
            self.snake_dir = new_dir

    def go_left(self, event):
        self.change_direction("Left")

    def go_right(self, event):
        self.change_direction("Right")

    def go_up(self, event):
        self.change_direction("Up")

    def go_down(self, event):
        self.change_direction("Down")

if __name__ == "__main__":
    SnakeGame()
