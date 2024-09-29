print("==============================================")
print("         Menu - Joshua Chew Chun Thoe         ") #print()
print("==============================================")
print("1. Add")
print("2. Minus")
print("3. Multiply")
print("4. Divide")

# Reading an integer input from the user
Option = int(input("Enter your option: "))

# If-else Statements
if Option == 1:
    print("Your action is adding value.")

    total_add = 0
    Add_Value = 10
    while Add_Value != 0:
        Add_Value = int(input("Enter your adding number: "))
        # If the user enters 0, break the loop

        #Calculation
        total_add += Add_Value   #total_add = total_add + Add_Value     A=A+B
        print("The total value is " , total_add)
    #End The calculation
    print("The calculation is ended.")

elif Option == 2:
    print("Your action is minus value.")
    Minus_Value1 = int(input("Enter your minus number 1: "))
    Minus_Value2 = int(input("Enter your minus number 2: "))
    #Calculations
    total_minus = Minus_Value1 - Minus_Value2
    print("Total minus value is ", total_minus)


elif Option == 3:
    print("Your action is multiply value.")
    Add_Value = 10

    #Giving ur 1st multiply number
    total_add = int(input("Enter your multiply number: "))

    while Add_Value != 0:
        Add_Value = int(input("Enter your multiply number: "))
        # If the user enters 0, break the loop
        if Add_Value == 0:
            #End the Loop
            break

        # Calculation
        total_add *= Add_Value  # total_add = total_add + Add_Value     A=A+B
        print("The total value is ", total_add)
    # End The calculation
    print("The total value is ", total_add)
    print("The calculation is ended.")

elif Option == 4:
    print("Your action is divide value.")
    #Enter the value
    loop_times = int(input("Enter your divide times: "))
    Divide1 = int(input("Enter your divide value: "))

    #Declare value of J
    j = 0

    #For Loop - How many times you need to loop
    for j in range(loop_times):    # j = start, value = 1 | loop_times = 5 | j + 1
        Divide2 = int(input("Enter your divide value: "))
        Divide1 = Divide1 / Divide2

        #Show the Divide value
        print("The Current Value after Divide is " , Divide1)

    #End Calculation
    print("==========================End of Calculation============================")

elif Option == 5:
        print("Your action is multiply.")
        # ANSI escape codes for red text
        RED = "\033[96m"
        RESET = "\033[0m"  # Reset to default color

        #Validation for variable 1
        while True:  # Start an infinite loop
            try:
                # Prompt the user to enter a value
                multiply1 = input("Enter a number (enter a non-numeric value to exit): ")

                # Try to convert the input to an integer
                value = int(multiply1)

                # If conversion is successful, break the loop
                print(f"You entered the number: {value}")
                break  # Exit the loop if the input is valid

            except ValueError:
                # Handle the case where the input is not an integer
                print(f"{RED}Error: Please enter a valid integer.{RESET}")
                print(ValueError)

        # Validation for variable 2
        while True:  # Start an infinite loop
            try:
                # Prompt the user to enter a value
                multiply2 = input("Enter a number (enter a non-numeric value to exit): ")

                # Try to convert the input to an integer
                value2 = int(multiply2)

                # If conversion is successful, break the loop
                print(f"You entered the number: {value2}")
                break  # Exit the loop if the input is valid

            except ValueError:
                # Handle the case where the input is not an integer
                print(f"{RED}Error: Please enter a valid integer.{RESET}")


        total_value = value*value2
        print("Your multiply value is ", total_value)


else:
    print("Error! Your input value is wrong! Please type again!")