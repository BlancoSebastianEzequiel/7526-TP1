from math import erf, sqrt, log
from src.problem_3 import generate_normal


def _F(values, x, accumulated_sum, cumulative_pos, n):
    """:param values: array of sorted numeric values"""
    for i in range(cumulative_pos, n):
        if values[i] <= x:
            accumulated_sum += 1
        else:
            return accumulated_sum, i
        cumulative_pos = i
    return accumulated_sum, cumulative_pos


def F(x, mu, sigma):
    return (1 + erf((x-mu)/(sqrt(2)*sigma))) / 2


def actual_distribution_distance(values, mu, sigma):
    max_value = None
    accumulated_sum = 0
    cumulative_pos = 0
    n = len(values)
    for x in values:
        accumulated_sum, cumulative_pos = \
            _F(values, x, accumulated_sum, cumulative_pos, n)
        q = abs(accumulated_sum/n - F(x, mu, sigma))
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
