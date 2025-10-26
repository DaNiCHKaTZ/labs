import numpy as np
import os
import sys
from PIL import Image as img

def get_line(start, end):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    is_steep = abs(dy) > abs(dx)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
    if swapped:
        points.reverse()
    return points

# Чтение аргументов
if len(sys.argv) < 5:
    print("Usage: python 1.py x1 y1 x2 y2")
    sys.exit(1)

start = [int(sys.argv[1]), int(sys.argv[2])]
end = [int(sys.argv[3]), int(sys.argv[4])]
L = get_line((start[0], start[1]), (end[0], end[1]))

matrix = np.ones((1000, 1000), dtype=np.uint8)
for i, j in L:
    matrix[i][j] = 0

im = img.fromarray(255 * matrix, mode='L')
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'line.png')
im.save(fp=file_path)
