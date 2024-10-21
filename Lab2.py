import math

def display_main_menu():
    inp=input("Enter some numbers separated by commas (e.g. 5, 67, 32): ")
    return inp
def get_user_input():
    inputs= display_main_menu()
    string_numbers=inputs.split(',')
    numbers=[]
    for num in  string_numbers:
        numbers.append(float(num))
    return numbers


def calc_average_temperature(numbers):
      return  sum(numbers)/len(numbers)
def calc_min_temperature(numbers):
    return min(numbers)
def calc_max_temperature(numbers):
    return max(numbers)



def display():
    numbers = get_user_input()
    average=round(calc_average_temperature(numbers),2)
    maximum=calc_max_temperature(numbers)
    minimum=calc_min_temperature(numbers)

    print("Average temperature: "+str(average))
    print("Maximum temperature: "+str(maximum))
    print("Minimum temperature: "+str(minimum))


display()

if __name__=="__main__":
    display()