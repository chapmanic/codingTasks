num1 = int(input("Please enter Your Three Event Times (In Minutes), Swimming Event: "))
num2 = int(input("Cycling Event: "))
num3 = int(input("Running Event: "))
time = num1 + num2 + num3
print(f"Your total triathlon time was: {time}")
if time <= 100:
    print("Provincial Colours")
elif time <= 105 and time >= 101:
    print("Provincial Half Colours")
elif time <= 110 and time >= 106:
    print("Provincial Scroll")
else:
    print("No Award")