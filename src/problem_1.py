import matplotlib.pyplot as plt


# Informar los primeros 10 números generados.
def gcl(seed=10, iterations=10, multiplier=1013904223, addition=1664525, module=232, normalize=False):
    results = []
    x = seed
    for _ in range(iterations):
        results.append(x)
        x = (multiplier * x + addition) % module

    if not normalize:
        return results
    return [x / (module - 1) for x in results]


if __name__ == "__main__":
    print('Parte 1: \n')
    print(gcl())

    # Modificar el GCL para que devuelva números al azar entre 0 y 1
    print('\nParte 2:')
    print(gcl(normalize=True))


# Realizar un histograma mostrando 100.000 valores generados en el punto b.
def gcl_with_histogram(seed=10, iterations=10, multiplier=1013904223, addition=1664525, module=232, normalize=False):
    results = gcl(seed, iterations, multiplier, addition, module, normalize)
    bins = [bin / 10 for bin in range(10)]

    plt.hist(results, bins)
    plt.show()


if __name__ == "__main__":
    gcl_with_histogram(iterations=100000, normalize=True)
