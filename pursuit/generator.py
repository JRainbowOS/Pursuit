import numpy as np

def direction_generator(start_x, start_y, dx, dy):
    direction = np.array([start_x, start_y])
    while True:
        yield direction
        direction += np.array([dx, dy])

def angle_generator(start_angle, increment):
    angle = start_angle
    while True:
        yield angle % (2 * np.pi)
        angle += increment 
        
start_x, start_y = 0, 0
dx, dy = 1, 2

# g = direction_generator(start_x, start_y, dx, dy)
g = angle_generator(0, 1)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# for elem in g:
#     print(elem)
    