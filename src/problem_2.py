import matplotlib.pyplot as plt
import numpy as np

from src.problem_1 import gcl


def generate_f(lambda_):
    def f_(t):
        if 0 <= t < 10:
            return 1 / 25
        elif 10 <= t:
            return (3 / 5) * lambda_ * np.exp(lambda_ * (10 - t))
        else:
            raise Exception('f: t has to be positive or zero')

    return f_


def generate_F(lambda_):
    def F_(t):
        if 0 <= t < 10:
            return (1 / 25) * t
        elif 10 <= t:
            return -3 / 5 * np.exp(lambda_ * (10 - t)) + (10 / 25 + 3 / 5)
        else:
            raise Exception('F: t has to be positive or zero')

    return F_


def generate_inv_F(lambda_):
    def inv_F_(t):
        if 0 <= t < 10 / 25:
            return 25 * t
        elif 10 / 25 <= t <= 1:
            return 10 - (1 / lambda_) * np.log((5 / 3) * ((10 / 25) + (3 / 5) - t))
        else:
            raise Exception('inv_F: t has to be between 0 and 1')

    return inv_F_


def x_values(start, end, step):
    return [step * x_ for x_ in range(start, 1 + int(end / step))]


def y_values(x_values_, function):
    return [function(x_) for x_ in x_values_]


if __name__ == "__main__":
    _lambda = 1 / 15

    x = x_values(start=0, end=250, step=0.5)

    plt.plot(x, y_values(x, function=generate_f(_lambda)))
    plt.xlabel('f(x)')
    plt.show()

    plt.plot(x, y_values(x, function=generate_F(_lambda)))
    plt.xlabel('F(x)')
    plt.show()

    x = x_values(start=0, end=0.999, step=0.001)

    plt.plot(x, y_values(x, function=generate_inv_F(_lambda)))
    plt.xlabel('inv_F(x)')
    plt.show()

    sample_count = 100000
    inv_F = generate_inv_F(_lambda)
    f_random_samples = [inv_F(random) for random in gcl(normalize=True, iterations=sample_count)]
    plt.hist(f_random_samples, bins=100)
    plt.show()
