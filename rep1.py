from aluLib import *

window_height = 600
window_width = 1000


def niger():
    set_fill_color(1, 0, 0)
    rectangle_height = window_height / 3
    draw_rectangle(0, 0, window_width, rectangle_height)
    set_fill_color(0, 1, 0)
    draw_rectangle(0, rectangle_height * 2, window_width, rectangle_height)
    set_fill_color(1, 0, 0)
    draw_circle(500, 300, 80)


start_graphics(niger, width=window_width, height=window_height)
