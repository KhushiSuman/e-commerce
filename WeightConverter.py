Pound = 2.20462
Kilogram = 1
weightF = input("Enter L for lbs or K for kilogram ")
weight = int(input("Enter your weight "))
if weightF == "L" or "l":
    print("Your weight in kilogram is: ", weight / Pound)
elif weightF == "K" or "k":
    print("Your weight in lbs is ", Pound * weight)
else:
    print("Wrong option chosen please choose again. Thank You!")
