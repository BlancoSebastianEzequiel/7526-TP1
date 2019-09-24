from math import sqrt, exp, pi
import numpy as np
from numpy.random import exponential, rand, normal
import matplotlib.pyplot as plt
from time import time


def normal_distribution(x, mu, sigma):
    exponent = (-1) * (x - mu) ** 2 / (2 * (sigma ** 2))
    scalar = 1/(sigma * sqrt(2 * pi))
    return scalar * exp(exponent)


def exponential_distribution(y, _lambda):
    return _lambda * exp((-1) * _lambda * y)


def c_value(mu, sigma, _lambda):
    t = sigma ** 2 * _lambda
    f_x_t = normal_distribution(t, mu, sigma)
    f_y_t = exponential_distribution(t, _lambda)
    return f_x_t/f_y_t


def generate_normal(mu, sigma, _lambda, n):
    samples = exponential(1 / _lambda, n)
    c = c_value(mu, sigma, _lambda)
    f_x = lambda x: normal_distribution(x, 0, sigma)
    f_y = lambda x: exponential_distribution(x, _lambda)
    p = [f_x(t)/(c * f_y(t)) for t in samples]
    z = []
    percentage_of_rejections = 0
    total = 0
    i = 0
    while i < n:
        if rand() >= p[i]:
            percentage_of_rejections += 1
            total += 1
            continue
        if rand() < 0.5:
            z.append(samples[i])
        else:
            z.append((-1)*samples[i])
        total += 1
        i += 1
    percentage_of_rejections = percentage_of_rejections / total
    z = [_z+mu for _z in z]
    return z, percentage_of_rejections


def map_relative_frequencies(values):
    size = len(values)
    freq = {}
    for val in values:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 0
    return list(map(lambda x: float(x/size), freq.values()))


def relative_frequency_histogram(plt, values):
    return plt.hist(values, histtype='barstacked', density=True)


def graph_normal_density_function(plt, mu, sigma, n):
    x = normal(loc=mu, scale=sigma, size=n)
    x.sort()
    y = [normal_distribution(t, mu, sigma) for t in x]
    label = 'normal'
    plt.plot(x, y, color='C2', label=label, ls='--')
    plt.legend(loc='upper right')


if __name__ == "__main__":
    mu = 15
    sigma = 3
    variance = sigma**2
    _lambda = 0.5
    n = 100000
    start = time()
    normal_values, percentage_of_rejections = generate_normal(mu, sigma, _lambda, n)
    time_elapsed = time() - start
    print(f"time elapsed: {time_elapsed} seconds")
    plt.figure(figsize=(5, 5))
    relative_frequency_histogram(plt, normal_values)
    graph_normal_density_function(plt, mu, sigma, n)
    plt.show()
    actual_mean = np.mean(normal_values)
    mean_error = abs(mu - actual_mean)
    print(f"mu: {actual_mean} - error: {mean_error}")
    actual_variance = np.std(normal_values, ddof=1)**2
    variance_error = abs(variance - actual_variance)
    print(f"actual sigma: {actual_variance} - error: {variance_error}")
    print(f"percentage_of_rejections: {percentage_of_rejections}")
