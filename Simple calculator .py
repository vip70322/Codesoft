# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the comparison choices
print("\nSelect a comparison operation:")
print("1. Equal to (==)")
print("2. Not equal to (!=)")
print("3. Greater than (>)")
print("4. Less than (<)")
print("5. Greater than or equal to (>=)")
print("6. Less than or equal to (<=)")

# Get the user's choice
choice = input("Enter your choice (1/2/3/4/5/6): ")

# Perform the selected comparison
if choice == '1':
    print(f"\nIs {num1} equal to {num2}? : {num1 == num2}")
elif choice == '2':
    print(f"\nIs {num1} not equal to {num2}? : {num1 != num2}")
elif choice == '3':
    print(f"\nIs {num1} greater than {num2}? : {num1 > num2}")
elif choice == '4':
    print(f"\nIs {num1} less than {num2}? : {num1 < num2}")
elif choice == '5':
    print(f"\nIs {num1} greater than or equal to {num2}? : {num1 >= num2}")
elif choice == '6':
    print(f"\nIs {num1} less than or equal to {num2}? : {num1 <= num2}")
else:
    print("\nInvalid choice. Please select a number between 1 and 6.")
