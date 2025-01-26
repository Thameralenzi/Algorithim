class GCDCalculator:
    """this class uses the euclidean algorithm to find the gcd of two positive integers  """
  
    def calculate_gcd(x, y):
        """this method finds the gcd of two positive numbers using the euclidean algorithm
        and returns the gcd"""
        
        while y != 0:
            temp = y
            y = x % y  # find the remainder
            x = temp  # set 'x' to the previous value of 'y'
        return x
    
