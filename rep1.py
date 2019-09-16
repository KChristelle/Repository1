from aluLib import *

window_height = 600
window_width = 1000


def nigeria():
    set_fill_color(0, 0.53, 0.32)
    rectangle_width =window_width/3
    draw_rectangle(0, 0, rectangle_width, window_height)
    draw_rectangle(rectangle_width*2, 0, rectangle_width, window_height)


start_graphics(nigeria, width=window_width, height=window_height)