w=float(input("Enter your weight "))
h=float(input("Enter your height "))
BMI=w/(h*h)
print("Your BMI is ",BMI)
if BMI<18.5:
    print("You are underweight")
elif BMI >=18.5 and BMI<24.9:
    print("You are healthy")
elif BMI >=25 and BMI<29.9:
    print("You are overweight")
else:
    print("You are obese")            