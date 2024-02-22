def add(a, b):
    return a + b

def calculate_factors_of_number(number):
    return [factors for factors in range(1, number) if number % factors == 0]

def perfect_number_check(number):
    factors_of_number = (calculate_factors_of_number(number))

    sum_of_factors = sum(factors_of_number)

    return sum_of_factors == number
