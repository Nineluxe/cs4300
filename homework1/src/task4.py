
def calculate_discount(startingPrice, discountPercentage):
    startingPrice = float(startingPrice)
    discountPercentage = float(discountPercentage)

    if (discountPercentage > 1.0):
        discountPercentage /= 100.0

    finalPrice = startingPrice - (startingPrice * discountPercentage)
    return finalPrice

print(calculate_discount(15, 0.5))