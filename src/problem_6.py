import matplotlib.pyplot as plt

from problem_1 import gcl


def transformation_method_generator(iterations):
    uniform_values = gcl(normalize=True, iterations=iterations)

    final_values = []
    for x in uniform_values:
        if 0 <= x < 0.1:
            value = 1
        elif 0.1 <= x < 0.6:
            value = 2
        elif 0.6 <= x < 0.9:
            value = 3
        else:
            value = 4
        final_values.append(value)

    return final_values


if __name__ == "__main__":
    plt.hist(transformation_method_generator(100000))
    plt.show()
