import validators

# Uses validators package to determine the validity of an input URL
def isURL(testURL):
    """ Returns a boolean reflecting the validity of the input URL. """
    validURL = True if validators.url(testURL) else False
    return validURL

