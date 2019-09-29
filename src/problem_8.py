from problem_1 import gcl
from problem_9 import chi_square_test

def gaps_calculator(sample, segment):
    gaps_target = []
    target_counter = 0
    target_start_counting = False

    for value in sample:
        if target_start_counting: target_counter += 1 

        if (segment[0] <= value and value <= segment[1]):
            if not target_start_counting:
                target_start_counting = True
            else:
                gaps_target.append(target_counter - 1) # Save the distance between repetitions
                target_counter = 0
    
    return gaps_target

def probablility_for(p0, gap):
    return p0 * ((1 - p0)**gap)

def check_result(chi_square_result, threshold, precent):
    print('Considerando un nivel de significancia del',precent,'%: \n')
    if(chi_square_result < threshold): 
        print('Se acepta la hipotesis \n')
    else:
        print('Se rechaza la hipotesis \n')

if __name__ == "__main__":
    one_percent_threshold = 44.314
    five_percent_threshold = 37.652

    sample = gcl(normalize=True, iterations=100000)

    segment = (0.3, 0.6)

    p0 = segment[1] - segment[0]

    print('Realizando Gap Test para distribucion Uniforme del problema 1 utilizando el intervalo [0.3 - 0.6]\n')
    gaps_target = gaps_calculator(sample, segment)

    categories = list(set(gaps_target))

    expected_for_category = [ probablility_for(p0, category) * len(gaps_target) for category in categories ]

    chi_square_result = chi_square_test(gaps_target, expected_outcomes= expected_for_category)

    print('Resultado del test: ', chi_square_result)

    check_result(chi_square_result, one_percent_threshold, 1)

    check_result(chi_square_result, five_percent_threshold, 5)
