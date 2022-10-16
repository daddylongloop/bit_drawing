#!/bin/python
from turtle import *
from funcs import *
from random import randint

n_bits = int(input("how many bits to draw (whole number): "))
bgcolor("blue")
title("Random Binary Num")
t = Turtle()
t.width(10)

"""
Will use a while/for loop to generate the origin values hopefully from right to left
"""


bits = []
for _ in range(n_bits):
    bits.append(randint(0, 1))
i = 0
y = 0
for x in range(400, -400, -30):
    if i > len(bits) - 1:
        i = 0
        break
    if bits[i] == 1:
        draw_one(t, (x, y))
    else:
        draw_zero(t, (x, y))
    i += 1

num = ""
for bit in bits:
    num = num + str(bit)
num = int(num, 2)


print("The Number Was:", num)
done()
