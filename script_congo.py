from aluLib import *

window_height = 600
window_length = 1000


def congo():
    set_fill_color(0, 0.6, 0)
    draw_triangle(x1=0, y1=0, x2=0, y2=window_height, x3=700, y3=0)
    set_fill_color(1, 0, 0)
    draw_triangle(x1=window_length, y1=window_height, x2=window_length, y2=0, x3=0, y3=window_length)
    set_clear_color(0, 0.6, 0)



start_graphics(congo, width=window_length, height=window_height)
