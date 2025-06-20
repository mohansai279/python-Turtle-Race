from turtle import Turtle, Screen
import random

# Ask for number of turtles from the terminal (no try-except)
num_turtles = input("Enter number of turtles (2 to 10): ")

# Check if the input is a digit and within range
if num_turtles.isdigit():
    num_turtles = int(num_turtles)
    if num_turtles < 2 or num_turtles > 10:
        print("Please enter a number between 2 and 10.")
        exit()
else:
    print("Invalid input. Please enter a number between 2 and 10.")
    exit()

# Setup turtle screen
screen = Screen()
screen.setup(width=800, height=400)
screen.title("Turtle Race")

# List of turtle colors
colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink', 'yellow', 'cyan', 'brown', 'magenta']
random.shuffle(colors)

# Create turtles
turtles = []
start_x = -350
start_y = -100
gap = 200 / (num_turtles - 1)

for i in range(num_turtles):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(start_x, start_y + i * gap)
    turtles.append(t)

# Start race
finish_line = 350
winner = None
race_on = True

while race_on:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() >= finish_line:
            winner = t.pencolor()
            race_on = False
            break

# Print winner in terminal
print(f"\n🏁 The winner is: {winner.upper()}!")

# Wait for click to close turtle screen
screen.exitonclick()
