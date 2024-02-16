# Create a variable which will select the number of rows
rows = 5

# Use a for loop to set the range, which is double rows
for i in range(1, rows * 2):  # Loop to cover the increase and decrease
    if i <= rows:
        print("*" * i)  # Print * times i, until i reaches value fo row 
    else:
        # Now print descending * based on ascending value, skipping row value. Using fixed fow value minus i.
        print("*" * (rows * 2 - i))
