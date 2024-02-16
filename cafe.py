# One menu list with four items, index 0-3
menu = ["sandwich", "burger", "fries", "ice cream"]

# Two dictionaries with Key, Value pairs. Referencing Menu items. 
stock = {"sandwich": 4, "burger": 43, "fries": 55, "ice cream": 54}
price = {"sandwich": 4.5, "burger": 6.50, "fries": 3.5, "ice cream": 4}

# A for loop which loops over each item in the menu list. 
# Total stock variable declared and set to 0
total_stock = 0
# Item acts as an iteration through the menu e.g. 0-3
for item in menu:
    # Variable which calculates stores the stock item times (*) the price
    value = (stock[item] * price[item])
    # Add value to total stock
    total_stock += value
    print(f"{item}: £{value:.2f}")
# Print total stock
print(f"Total stock worth: £{total_stock:.2f}")