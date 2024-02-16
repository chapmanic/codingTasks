numbers = []
running_ = True
while running_:
    user_ = int(input("Please enter a number (or -1 to stop): "))
    if user_  >= 0:
        numbers.append(user_)
    else:
        running_ = False
        print(sum(numbers) / (len(numbers)))