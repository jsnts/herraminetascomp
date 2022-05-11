"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

fooden = [vector(-10,0)]
snake = [vector(10, 0)]
aim = vector(0, -10)
aimem = vector(10,10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def changeen():
    aimem.x = randrange(-10,10)
    aimem.y = randrange(-10,10)


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def insidem(food):
    return -200 < food.x < 190 and -200 < food.y < 190

    




def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == fooden:
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    food = fooden[-1].copy()
    food.move(aimem)

    if not inside(food) or food in fooden:
        square(food.x,food.y,9,'green')
        update()
        return

    fooden.append(food)
    
    if food == fooden:
        print('Snake:', len(snake))
    else:
        fooden.pop(0)


    for body in fooden:
        square(body.x,body.y,9,'green')


    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
changeen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
