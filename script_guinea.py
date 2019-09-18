from aluLib import *

window_height = 600
window_length = 1000


def guinea():
    set_fill_color(1, 0, 0)
    rectangle_length = window_length / 3
    # defining the length of the rectangle which will be a third of the window's length
    draw_rectangle(0, 0, rectangle_length, window_height)
    set_fill_color(1, 1, 0)
    draw_rectangle(rectangle_length, 0, rectangle_length, window_height)
    # drew the second rectangle which it meant to be in the middle hence setting x to rectangle length
    set_fill_color(0, 0.4, 0)
    draw_rectangle(rectangle_length * 2, 0, rectangle_length, window_height)
    # drew the last rectangle which is meant to be at the last spot hence setting x to two times the rectangle length


start_graphics(guinea, width=window_length, height=window_height)
