weight = float(input("enter your weight: "))
height = float(input("enter your height:"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal")
elif 25 <= bmi < 30:
    print("overweight")
else:
    print("obesity")