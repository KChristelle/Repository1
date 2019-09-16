from aluLib import *

window_height = 600
window_width = 1000


def guinea():
    set_fill_color(1, 0, 0)
    rectangle_width = window_width / 3
    draw_rectangle(0, 0, rectangle_width, window_height)
    set_fill_color(1, 1, 0)
    draw_rectangle(rectangle_width * 1, 0, rectangle_width, window_height)
    set_fill_color(0, 0.4, 0)
    draw_rectangle(rectangle_width * 2, 0, rectangle_width, window_height)


start_graphics(guinea, width=window_width, height=window_height)
