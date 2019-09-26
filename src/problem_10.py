from math import erf, sqrt, log
from src.problem_3 import generate_normal


def _F(values, x):
    n = len(values)
    return sum(list(filter(lambda xi: xi <= x, values))) / n


def F(x, mu, sigma):
    return (1 + erf((x-mu)/(sqrt(2)*sigma))) / 2


def actual_distribution_distance(values, mu, sigma):
    max_value = None
    for x in values:
        q = abs(_F(values, x) - F(x, mu, sigma))
        if max_value is None or q > max_value:
            max_value = q
    return max_value


def reject_hypothesis(alpha, q, n):
    return q > sqrt((-1)*(1/(2*n))*log(alpha/2))


if __name__ == "__main__":
    _mu = 15
    _sigma = 3
    _lambda = 0.5
    _n = 100000
    normal_values, _ = generate_normal(_mu, _sigma, _lambda, _n)
    _q = actual_distribution_distance(normal_values, _mu, _sigma)
    h0 = reject_hypothesis(0.01, _q, _n)
    print(f"Test with significance level=0.01: {'OK' if h0 else 'Failed'}")
    if not h0:
        h0 = reject_hypothesis(0.05, _q, _n)
        print(f"Test with significance level=0.05: {'OK' if h0 else 'Failed'}")
