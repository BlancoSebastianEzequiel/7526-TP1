from math import sqrt, exp, pi
from numpy.random import exponential, rand
import matplotlib.pyplot as plt


def normal_distribution(x, mean, standard_deviation):
    exponent = (-1)*(x-mean)**2/(2*(standard_deviation**2))
    scalar = 1/(standard_deviation*sqrt(2*pi))
    return scalar * exp(exponent)


def exponential_distribution(y, lambda_value):
    return lambda_value * exp((-1)*lambda_value*y)


def c_value(mean, standard_deviation, lambda_value):
    t = standard_deviation**2*lambda_value
    f_x_t = normal_distribution(t, mean, standard_deviation)
    f_y_t = exponential_distribution(t, lambda_value)
    return f_x_t/f_y_t


def generate_normal(mean, standard_deviation, lambda_value, n):
    samples = exponential(1/lambda_value, n)
    c = c_value(mean, standard_deviation, lambda_value)
    f_x = lambda x: normal_distribution(x, mean, standard_deviation)
    f_y = lambda x: exponential_distribution(x, lambda_value)
    p = [f_x(t)/(c * f_y(t)) for t in samples]
    z = []
    i = 0
    while i < n:
        r = rand()
        if r >= p[i]:
            i += 1
            continue
        if rand() < 0.5:
            z.append(samples[i])
        else:
            z.append((-1)*samples[i])
        i += 1
    return z


normal = generate_normal(15, 3, 1, 100000)
size = len(normal)
plt.hist(normal)
plt.show()
