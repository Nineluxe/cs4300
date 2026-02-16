
def calculate_discount(startingPrice, discountPercentage):
    """ Takes a number of variable format (int, float or string) and returns the final price after increasing by a percentage. """
    # Converts arguments to floats
    startingPrice = float(startingPrice)
    discountPercentage = float(discountPercentage)

    # If the argument wasnt originally a float, convert it to a decimal to
    # easily calculate the percentage increase
    if (discountPercentage > 1.0):
        discountPercentage /= 100.0

    # Calculate the final price
    finalPrice = startingPrice - (startingPrice * discountPercentage)
    return finalPrice

