# ENGINEERING UNIT CONVERTER

# Store conversion history
history = []

# Function to perform conversions
def convert(value, choice):

    if choice == 1:
        return value / 25.4

    elif choice == 2:
        return value * 25.4

    elif choice == 3:
        return (value * 9/5) + 32

    elif choice == 4:
        return (value - 32) * 5/9

    elif choice == 5:
        return value * 2.20462

    elif choice == 6:
        return value / 2.20462

    elif choice == 7:
        return value / 3.6

    elif choice == 8:
        return value * 3.6


# Main program loop
while True:

    print("\nENGINEERING UNIT CONVERTER")
    print("1. mm to Inches")
    print("2. Inches to mm")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. kg to Pounds")
    print("6. Pounds to kg")
    print("7. km/h to m/s")
    print("8. m/s to km/h")
    print("9. View Conversion History")
    print("0. Exit")

    try:
        choice = int(input("Choose an option: "))

        if choice == 0:
            print("Thank you for using the converter!")
            break

        elif choice == 9:
            print("\nCONVERSION HISTORY")

            if len(history) == 0:
                print("No conversions yet.")

            else:
                for item in history:
                    print(item)

        elif choice >= 1 and choice <= 8:

            value = float(input("Enter the value: "))

            result = convert(value, choice)

            print("Result:", round(result, 2))

            record = str(value) + " = " + str(round(result, 2))
            history.append(record)

        else:
            print("Invalid option. Please choose 0 to 9.")

    except ValueError:
        print("Invalid input! Please enter a number.")