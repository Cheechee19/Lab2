import math
def calculate_bmi (height, weight):
    print ("Height: "+ str(height))
    print ("Weight: "+ str(weight))
    bmi= round(weight/height**2,2)
    print(f"Your bmi is {bmi}")
    if bmi<18.5:
        print("You are underweight")
        return -1
    elif bmi>25:
        print("You are over weight")
        return 1
    else:
        print("You are normal weight")
        return 0

calculate_bmi(1.73,30)
 