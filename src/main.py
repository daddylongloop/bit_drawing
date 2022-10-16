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
for i in range(n_bits):
    bits.append(randint(0, 1))
i = 0
used_i = []
for x in range(400, -400, -50):
    if i in used_i:
        break
    if i > len(bits) - 1:
        i = 0
        continue
    if bits[i] == 1:
        draw_one(t, (x, 0))
    else:
        draw_zero(t, (x+20, 0))
    used_i.append(i)
    i += 1

num = ""
for bit in bits:
    num = num + str(bit)
num = int(num, 2)


print("The Number Was:", num)
done()
