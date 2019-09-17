import matplotlib.pyplot as plt

# Informar los primeros 10 números generados.
def gcl(seed = 10, iterations = 10, multiplier = 1013904223, addition = 1664525, module = 232):
  x = seed
  for _ in range(iterations):
    x = (multiplier * x + addition) % module
    print(x)

print('Parte 1: \n')
gcl()

# Modificar el GCL para que devuelva números al azar entre 0 y 1
def gcl2(seed = 10, iterations = 10, multiplier = 1013904223, addition = 1664525, module = 232):
  x = seed
  for _ in range(iterations):
    x = ((multiplier * x + addition) % module) / module
    print(x)

print('\nParte 2:')
gcl2()

# Realizar un histograma mostrando 100.000 valores generados en el punto b.
def gcl_with_histogram(seed = 10, iterations = 10, multiplier = 1013904223, addition = 1664525, module = 232):
  results = []
  x = seed
  for _ in range(iterations):
    x = ((multiplier * x + addition) % module) / module
    results.append(x)

  bins = [ bin / 10 for bin in range(10) ]
  plt.hist(results, bins)
  plt.show()

gcl_with_histogram(iterations= 100000)
