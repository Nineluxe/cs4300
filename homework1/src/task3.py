import math

# Returns the sign of the value in string form
def getSign(num):
    """ Returns a string, either: error, Positive, Negative, or Zero, based on the input number."""
    # Verify this input is a number
    if not isinstance(num, (int, float)):
        return "error"
    
    # Check for cases
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    
    return "error"

# Generates a list of the first 10 prime numbers
def printFirst10Primes():
    """ Prints the first 10 prime numbers. """
    # Check if the given number is prime
    def isPrime(num):
        if num < 2:
            return False
        
        # Check for no remainders up to the square root of num
        for i in range(2, math.floor(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        
        return True

    # Initialize list
    primeList = []
    p = 2
    
    # Fill the list as long as the length is less than n
    while (len(primeList) < 10):
        if isPrime(p):
            primeList.append(p)
        p += 1

    for i in primeList:
        print(i, end=" ")


# Summation of numbers from 1 - 100
def sum1To100():
    """ Returns a summation of all numbers from 1 to 100. """
    num = 1
    count = 1
    while (count < 100):
        count += 1
        num += count

    return num
