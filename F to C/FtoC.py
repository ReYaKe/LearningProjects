while True:
    choice = input("Type Fahrenheit to calculate Fahrenheit into Celsius or Celsius to calculate Celsius into Fahrenheit or Exit to exit the program:\n").lower()
    # User types in if they want C -> F or F -> C and converts it to lowercase
    if choice == "celsius" or choice == "c":
        try:
            F = input("Put in a degree Fahrenheit: \n")
            F = float(F)        # convert input to float so it can be calculated
            C = (F-32) * 5/9    # Conversion Formula
            print(f"Your degree Celsius is: {C:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for Fahrenheit.")
    elif choice == "fahrenheit" or choice == "f":
        try:
            C = input("Put in a degree Celsius: \n")
            C = float(C)        # convert input to float so it can be calculated
            F = C*9/5 +32       # Conversion Formula
            print(f"Your degree Fahrenheit is: {F:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for Celsius.")
    elif choice == "exit":
        print("Exiting the program.")
        break
    else: 
        print("\n")