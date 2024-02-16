# Create three user prompts, using .lower() function to ensure consistency when interacting with if/else statement 
city_flight = input("What city are you flying to? ").lower()
num_nights = int(input("How many nights are you staying for? "))
rental_days = int(input("How many days will you be hiring a car? "))

# Use a dictionary to store values, supporting easier data changes (or even future API linkup!)
costs_ = {"hotel_price": 68, "car_rental": 44 }

def hotel_cost(num_nights):
    """Calculate and return the total hotel cost."""
    y = num_nights * costs_["hotel_price"]
    return y

def plane_cost(city_flight):
    """Return the plane cost based on the destination city."""
    if city_flight == "paris":
        return 150
    elif city_flight == "berlin":
        return 180
    elif city_flight == "rome":
        return 210
    else:
        # Return a zero to avoid error
        print("No flight price data")
        return 0 

def car_rental(rental_days):
    """Return the total car rental cost."""
    return 44 * rental_days

def holiday_cost(hotel, flight, car):
    """Calculate and return the total cost of the holiday."""
    return hotel + flight + car

# Calculate costs based on user inputs.
total_hotel_cost = hotel_cost(num_nights)
total_flight_cost = plane_cost(city_flight)
total_car_cost = car_rental(rental_days)

# Print the total costs to the user.
print(f"Hotel cost: £{total_hotel_cost}")
print(f"Your flight will cost: £{total_flight_cost}")
print(f"Total car rental cost: £{total_car_cost}")

# print("The total cost of your holiday will be: £" + str(holiday_cost(total_hotal_cost, total_flight_cost, total_car_cost)))
print(f"The total cost of your holiday will be: £{holiday_cost(total_hotel_cost, total_flight_cost, total_car_cost)}")