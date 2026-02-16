import validators

# Uses validators package to determine the validity of an input URL
def isURL(testURL):
    validURL = True if validators.url(testURL) else False
    return validURL

