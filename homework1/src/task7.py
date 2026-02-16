import validators

def isURL(testURL):
    validURL = True if validators.url(testURL) else False
    return validURL

