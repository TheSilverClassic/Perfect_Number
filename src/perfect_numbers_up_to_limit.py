from src.perfect_number_checker import perfect_number_check

def perfect_numbers_up_to_limit(number):
    list_of_perfect_numbers = [numbers for numbers in range(1, number + 1) if perfect_number_check(numbers)]
    return list_of_perfect_numbers
