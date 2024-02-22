from src.perfect_numbers_up_to_limit import perfect_numbers_up_to_limit

def get_user_input():
    while True:
        try:
            number_limit = int(input("Please enter a number greater than or equal to 1: "))

            if number_limit >= 1:
                return number_limit

            else:
                print("Please enter a number greater than or equal to 1.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("The Perfect Number Finder")

    number_limit = get_user_input()

    list_of_perfect_numbers = perfect_numbers_up_to_limit(number_limit)

    print(f"Here are the perfect numbers from 1 to {number_limit}: {list_of_perfect_numbers}")

if __name__ == "__main__":
    main()
