print("Welcome to Car Rental System")
print("-" * 30)

# Get user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
license_valid = input("Do you have a valid license? (yes/no): ").lower()
rental_days = int(input("How many days do you want to rent? "))

# Car selection
print("\nAvailable Cars:")
print("1. Economy Car - $30/day")
print("2. Luxury Car - $100/day")
car_choice = int(input("Choose car type (1 or 2): "))

# Calculate rental cost
if car_choice == 1:
    car_type = "Economy"
    daily_rate = 30
else:
    car_type = "Luxury"
    daily_rate = 100

total_cost = daily_rate * rental_days

# Check eligibility using AND, OR, != operators
if age >= 21 and license_valid == "yes" and rental_days != 0:   
    print("\n--- Rental Summary ---")
    print(f"Name: {name}")
    print(f"Car Type: {car_type}")
    print(f"Rental Duration: {rental_days} days")
    print(f"Total Cost: ${total_cost}")
    
    # Additional discount conditions
    if rental_days > 7 or total_cost > 500:
        discount = total_cost * 0.10
        final_cost = total_cost - discount
        print(f"10% Discount Applied: -${discount}")
        print(f"Final Cost: ${final_cost}")
    
elif age < 21:
    print("Sorry, you must be 21 or older to rent a car")
elif license_valid != "yes":
    print("You must have a valid license to rent a car")
else:
    print("Invalid rental duration")