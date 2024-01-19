# day2\BMI_calculator.py
weight = int(input("enter your weight :"))
h = int(input("enter your height in cm :"))

height = h / 100

bmi = weight / (height * height)
BMI = round(bmi, 2)
if BMI <= 18.4:
    print("your BMI is ", BMI, "you are underweight")
elif BMI >= 18.5 and BMI <= 24.8:
    print("your BMI is ", BMI, "you are normal")
elif BMI >= 24.9 and BMI <= 29.9:
    print("your BMI is ", BMI, "you are overweight")
else:
    print("your BMI is ", BMI, "you are obese")