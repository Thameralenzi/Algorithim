class GCDCalculator:
    """this class calculates the gcd of two positive integers using the euclidean algorithm."""

    def calculate_gcd(x, y):
        """this method uses the euclidean algorithm to calculate and return the gcd of two numbers."""
        
        while y != 0:
            temp = y  # store the value of 'y'
            y = x % y  # calculate the remainder
            x = temp  # update 'x' to the previous value of 'y'
        return x
    def check_prime(x, y):
        """this method checks if two numbers have a gcd of 1"""
        return GCDCalculator.calculate_gcd(x, y) == 1
# # let us try our own selves
# try first input 100 and the second input 80 for example
def get_input():
    """this function gets input from the user and calculates the gcd"""
    
    num1 = int(input("please enter the first positive number: "))
    num2 = int(input("please enter the second positive number: "))

    # check if the inputs are valid positive numbers
    if num1 <= 0 or num2 <= 0:
        print("error, both numbers must be positive.")
        return 0
    return (num1, num2)

# main part of the program
input_data = get_input()
if input_data != 0:
    gcd_result = GCDCalculator.calculate_gcd(input_data[0], input_data[1])
    print(f"the gcd of {input_data[0]} and {input_data[1]} is: {gcd_result}")
    
    # check if the numbers have a gcd of 1
    if GCDCalculator.check_prime(input_data[0], input_data[1]):
        print(f"{input_data[0]} and {input_data[1]} have a gcd of 1.")
    else:
        print(f"{input_data[0]} and {input_data[1]} do not have a gcd of 1.")