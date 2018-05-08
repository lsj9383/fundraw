
# encoding: utf-8  

# def do(traces, rows, cols):
#   from matplotlib import pyplot as plt  
#   import numpy as np
#     plt.ion()
#     xs = []
#     ys = []
#     for trace in traces:
#         for p in trace:
#             #xs.append(p.col)
#             #ys.append(rows-p.row)
#             #plt.cla()
#             plt.scatter([p.col], [rows-p.row], c='black', s=1)
#             plt.xlim((0, cols))
#             plt.ylim((0, rows))
#             plt.axis('off')
#             plt.pause(0.001)

def do(traces, rows, cols, speed=10):
    import turtle

    turtle.pensize(2)
    turtle.up()
    turtle.speed(speed)
    for trace in traces:
        for p in trace:
            x = p.col - cols/2
            y = rows-p.row -rows/2
            turtle.goto(x, y)
            turtle.down()
            turtle.goto(x, y)
            turtle.up()