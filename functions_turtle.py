# Functions and Turtle
# Author: Lynn Kim
# 28 November 2023

import turtle

burt = turtle.Turtle()

burt.color("lightblue")


def squared(num: float) -> float:
    """Takes a number and squares and returns it."""

    return num**2


def draw_square(side_length: int) -> None:
    """Draw a square of a given length."""
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)
    burt.forward(side_length)
    burt.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 3. Turn turtle right
        burt.right(36 * 2)
        #    a. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        burt.left(36)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0])  # revert burt's colour


def draw_fancy_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height in pixels

    Params:

    level - number representing the levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Move turtle forward height pixels
        burt.forward(height)

        # 2. Turn turtle left
        burt.left(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.75)

        burt.right(36)
        draw_fancy_tree(level - 1, height * 0.75)

        # 3. Turn turtle right
        burt.right(36)
        #    a. Draw a smaller tree (current level - 1)
        draw_fancy_tree(level - 1, height * 0.75)

        # 4. Return to beginning
        burt.left(36)
        burt.back(height)
    else:
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0])  # revert burt's colour


def koch_edge(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [67, -134, 67, 0]:
            koch_edge(turtle, order - 1, size / 3)
            turtle.left(angle)


# Set-up Burt to draw trees
burt.color("brown")
# burt.setheading(90)  # points burt north
burt.pu()
burt.back(50)
burt.pd()
# burt.width(4)  # trunk and branches thicker
burt.speed(0)

# draw_fancy_tree(4, 175)

for i in range(3):
    koch_edge(burt, 2, 500)
    burt.right(120)

turtle.done()
