from aluLib import *

window_height = 600
window_length = 1000


def guinea():
    set_fill_color(1, 0, 0)
    rectangle_length = window_length / 3
    draw_rectangle(0, 0, rectangle_length, window_height)
    set_fill_color(1, 1, 0)
    draw_rectangle(rectangle_length * 1, 0, rectangle_length, window_height)
    set_fill_color(0, 0.4, 0)
    draw_rectangle(rectangle_length * 2, 0, rectangle_length, window_height)


start_graphics(guinea, width=window_length, height=window_height)
