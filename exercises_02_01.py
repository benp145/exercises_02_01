#Exercise 1

def calculator(first_number, second_number):
    print(f"\nYour numbers are {first_number} and {second_number}. Enter an operator you wish to perform on these numbers. Enter \"quit\" at any time to end program.")
    user_inp = ""
    while user_inp != 'quit':
        
        # take input for operator
        user_inp = input("Enter Operator: ")
        operator = user_inp
        
        if operator == "+":
            print(first_number + second_number)
        elif operator == "-":
            print(first_number - second_number)
        elif operator == "*":
            print(first_number * second_number)
        elif operator == "/":
            print(first_number / second_number)
        elif operator == "%":
            print(first_number % second_number)
        elif operator == "//":
            print(first_number // second_number)
        elif operator == "//":
            print(first_number // second_number)
        elif operator == "**":
            print(first_number ** second_number)
        else:
            print("Invalid operator! Try again.")

calculator(5,28)


#Exercise 2

def make_pyramid(n):
    for i in range(n):
        print((n-i-1)*" " + (2*i+1)*"X" + (n-i-1)*" ")

make_pyramid(1)
make_pyramid(2)
make_pyramid(3)
make_pyramid(4)
make_pyramid(5)
make_pyramid(6)