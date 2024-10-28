import math
def calculate_bmi (height, weight):
    print ("Height: "+ str(height))
    print ("Weight: "+ str(weight))
    bmi= round(weight/height**2,2)
    print(f"Your bmi is {bmi}")
    if bmi<18.5:
        print("You are underweight")
        x=-1
    elif bmi>25:
        print("You are over weight")
        x=1
    else:
        print("You are normal weight")
        x=0
    return x

calculate_bmi(1.73,30)
 