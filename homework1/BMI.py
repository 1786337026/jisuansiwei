height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI=weight/(height*height)
print("Your BMI is",BMI)
if BMI<18.5:
    print("过轻")
elif BMI<=25:
    print("正常")
elif BMI<=28:
    print("过重")
elif BMI<=32:
    print("肥胖")
else:
    print("严重肥胖")