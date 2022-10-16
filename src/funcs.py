#!/bin/python
"""
Drawing Functions
"""
if __name__ == "__main__":
    print('dont run this file !!')
    exit()


def _prepare(t, origin: tuple):
    """
    create origin coordinates and create length and width values
    also prepare the turtles color and starting coordinates
    takes turtle object and origin coordinates
    """
    t.up()
    ogX, ogY = origin
    y = 50
    t.goto(ogX, ogY)
    t.color('white')
    return (ogX, ogY, y)


def draw_zero(t, origin: tuple = (0, 0)):
    """
    Draws a zero with origin(tuple) coordinates
    takes in a turtle object
    """

    ogX, ogY, y = _prepare(t, origin)
    t.pendown()
    t.goto(ogX, y)
    t.goto(ogX-30, y)
    t.goto(ogX-30, ogY)
    t.goto(ogX, ogY)


def draw_one(t, origin: tuple = (0, 0)):
    ogX, _, y = _prepare(t, origin)
    bottomLineLength = 40
    t.pendown()
    t.goto(ogX, y)
