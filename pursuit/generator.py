import numpy as np

def direction_generator(start_x, start_y, dx, dy):
    direction = np.array([start_x, start_y])
    while True:
        yield direction
        direction += np.array([dx, dy])


start_x, start_y = 0, 0
dx, dy = 1, 0

g = direction_generator(start_x, start_y, dx, dy)
print(next(g))
print(next(g))
print(next(g))
# for elem in g:
#     print(elem)
    