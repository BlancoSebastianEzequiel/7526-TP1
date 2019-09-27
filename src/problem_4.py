import numpy as np
import math
import matplotlib.pyplot as plt

def random_square_coordinates(side_len, center, num_coords, angle):
    x_coords = []
    y_coords = []

    aux_center = side_len / 2
    rad_angle = np.radians(angle)
    cos_angle = np.cos(rad_angle)
    sin_angle = np.sin(rad_angle)
    for i in range(num_coords):
        x_coord = np.random.uniform(0, side_len)
        y_coord = np.random.uniform(0, side_len)
        x_coords.append((x_coord - aux_center) * cos_angle - (y_coord - aux_center) * sin_angle + center)
        y_coords.append((x_coord - aux_center) * sin_angle + (y_coord - aux_center) * cos_angle + center)

    return x_coords, y_coords


def plot_square(x_coords, y_coords):
    plt.plot(x_coords, y_coords, '.')
    plt.axis([0, 20, 0, 20])
    plt.show()

x_coords, y_coords = random_square_coordinates(5, 10, 100, 45)
plot_square(x_coords, y_coords)
