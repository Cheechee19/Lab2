import math

def get_user_input(user_input):
    string_numbers = user_input.split(',')
    numbers = []
    for num in string_numbers:
        numbers.append(float(num))
    return numbers

def calc_average_temperature(numbers):
    return sum(numbers) / len(numbers)

def calc_min_temperature(numbers):
    return min(numbers)

def calc_max_temperature(numbers):
    return max(numbers)

def calc_median_temperature(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 != 0:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    return median

def display(numbers):
    average = round(calc_average_temperature(numbers), 2)
    maximum = calc_max_temperature(numbers)
    minimum = calc_min_temperature(numbers)
    median = calc_median_temperature(numbers)

    return {
        "Average temperature": average,
        "Maximum temperature": maximum,
        "Minimum temperature": minimum,
        "Median temperature": median
    }

if __name__ == "__main__":
    user_input = input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    numbers = get_user_input(user_input)
    results = display(numbers)
    for key, value in results.items():
        print(f"{key}: {value}")