from aluLib import *

window_height = 600
window_length = 1000


def congo():
    set_fill_color(0, 0, 1)
    triangle_length = window_length - 3
    draw_triangle(x1=0, y1=0, x2=triangle_length, y2=window_height)


start_graphics(congo(), width=window_length, height=window_height)
