
# INTEGERS
# Converts a float to integer by dropping the decimal places
def floatToInt(float1):
    """
    Converts a float input to an integer

    Parameters:
        float1 (float): The first number.

    Returns:
        (int): float1 as an integer.
    """
    return int(float1)

# FLOATS
# Converts an integer to a floating point value (adds 0.0 to the integer)
def intToFloat(int1):
    """
    Converts the integer input to a float value.

    Parameters:
        int1 (int): The first number.

    Returns:
        (float): int1 as a float.
    """
    return float(int1)

# STRINGS
# Uses the indexing of string to return the final character of an input string
def getFinalChar(someString):
    """ Returns the final character of the input string. """
    return someString[len(someString) - 1]

# BOOLEANS
# Simply returns a boolean if the two arguments are equal
def isEqual(num1, num2):
    """ Returns a boolean reflecting whether or not the input numbers are equal. """
    return num1 == num2
