import numpy as np
from src.problem_6 import transformation_method_generator


def chi_square_test(random_values):
    values, observations = np.unique(random_values, return_counts=True)
    print('Cantidad de Observaciones', len(random_values))
    print('Observaciones: ', values, observations)
    expected_outcomes = np.divide(np.sum(observations), len(observations))
    print('Esperadas: ', expected_outcomes)
    print('Grados de libertad: ', len(observations) - 1)
    result = 0
    for observation in observations:
        result += (observation - expected_outcomes) ** 2 / expected_outcomes

    return result

def run_chi_square_test(threshold):
    random_values = transformation_method_generator(100)
    chi_square_result = chi_square_test(random_values)
    print('Resultado del Test: ', chi_square_result)
    print('Cuantíl: ', threshold)
    return chi_square_result < threshold


if __name__ == "__main__":
   one_percent_threshold = 11.3349
   five_percent_threshold = 7.8147

   print('Realizando Test Chi^2 - nivel significación: 1%\n')
   test_passed = run_chi_square_test(one_percent_threshold)

   if test_passed:
       print('\nSe acepta la hipótesis')
       exit(0)

   print('\nNo se acepta la hipótesis. \n\nRepitiendo Test - nivel de significación 5%\n')
   test_passed = run_chi_square_test(five_percent_threshold)
   if test_passed:
       print('\nSe acepta la hipótesis')
   else:
       print('\nNo se acepta la hipótesis')