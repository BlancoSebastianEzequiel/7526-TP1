from math import sqrt, cos, sin, log, pi
from random import random
import matplotlib.pyplot as plt
from src.problem_3 import \
    graph_normal_density_function, compare_mu, compare_variance


def generate_normal(iterations, callback, u1, u2):
    values = []
    for i in range(iterations):
        values.append(callback(u1[i], u2[i]))
    return values


def z0(t1, t2):
    return sqrt((-2)*log(t1)) * cos(2*pi*t2)


def z1(t1, t2):
    return sqrt((-2)*log(t1)) * sin(2*pi*t2)


def generate_pair(iterations):
    u1 = [random() for _ in range(iterations)]
    u2 = [random() for _ in range(iterations)]
    normal0 = generate_normal(iterations, z0, u1, u2)
    normal1 = generate_normal(iterations, z1, u1, u2)
    return normal0, normal1


if __name__ == "__main__":
    _iterations = 100000
    _normal0, _normal1 = generate_pair(_iterations)
    plt.figure(figsize=(5, 5))
    plt.hist(_normal0, histtype='barstacked', density=True)
    plt.hist(_normal1, histtype='barstacked', density=True)
    graph_normal_density_function(plt, 0, 1, _iterations)
    plt.show()
    print(f"compare variance and median for first normal values")
    compare_mu(_normal0, 0)
    compare_variance(_normal0, 1)
    print(f"compare variance and median for second normal values")
    compare_mu(_normal1, 0)
    compare_variance(_normal1, 1)
