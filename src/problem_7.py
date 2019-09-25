import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.problem_1 import gcl

Axes3D  # Importing this 'unused' class is necessary for some reason


def plot_2d(random_sample):
    plt.plot(random_sample[1:], random_sample[:-1], 'bo')
    plt.xlabel('X(n)')
    plt.ylabel('X(n-1)')
    plt.show()


def plot_3d(random_sample):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i in range(2, len(random_sample)):
        ax.scatter(
            random_sample[i - 2],
            random_sample[i - 1],
            random_sample[i]
        )

    ax.set_xlabel('X(n-2)')
    ax.set_ylabel('X(n-1)')
    ax.set_zlabel('X(n)')

    plt.show()


if __name__ == "__main__":
    _random_sample = gcl(iterations=50)
    plot_2d(_random_sample)
    plot_3d(_random_sample)
