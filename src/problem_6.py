import matplotlib.pyplot as plt

from src.problem_1 import gcl

uniform_values = gcl(normalize=True, iterations=100000)

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

plt.hist(final_values)
plt.show()
