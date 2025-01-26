class GCDCalculator:
    """this class calculates the gcd of two positive integers using the euclidean algorithm."""

    def calculate_gcd(x, y):
        """this method uses the euclidean algorithm to calculate and return the gcd of two numbers."""
        
        while y != 0:
            temp = y  # store the value of 'y'
            y = x % y  # calculate the remainder
            x = temp  # update 'x' to the previous value of 'y'
        return x