import math
def calculate_bmi (height, weight):
    print ("Height: "+ str(height))
    print ("Weight: "+ str(weight))
    bmi= round(weight/height**2,2)
    print(f"Your bmi is {bmi}")
    if bmi<18.5:
        print("You are underweight")
    elif bmi>25:
        print("You are over weight")
    else:
        print("You are normal weight")

calculate_bmi(1.73,30) 