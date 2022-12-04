from turtle import *
import math
import time
from PIL import Image

point_size = 5
screen_size = 500


def isPrime(number):
    if number >= 2:
        sqrt_value = int(math.sqrt(number)) + 1
        for i in range(2, sqrt_value):
            if number % i == 0:
                return False
        return True
    else:
        return False


def draw(color="white"):
    dot(point_size, color)
    fd(point_size + (int(point_size / 2)))


def draw_ulam():
    i = 1
    maxstep = 1
    step = 0
    turn = 2
    while abs(position()[0]) < window_height() / 2:
        if turn == 0:
            maxstep += 1
            turn = 2
        if isPrime(i):
            draw("white")
        else:
            fd(point_size + (int(point_size / 2)))

        step += 1
        if step >= maxstep:
            turn -= 1
            step = 0
            left(90)

        i += 1


bgcolor("black")
ht()
up()
title("Ulam spiral")
tracer(10)
setup(width=screen_size, height=screen_size, starty=1)


start = time.time()

draw_ulam()

print("Finished in : ", time.time() - start)
