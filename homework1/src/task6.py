
def wordCount():
    # Initialize file path
    filePath = 'homework1/task6_read_me.txt'

    # Read the contents of the file
    try:
        with open(filePath, 'r') as f:
            contents = f.read()
            
    except FileNotFoundError:
        print(f"Error: The file '{filePath}' was not found.")

    # Perform the word count
    count = 0
    words = contents.split()
    for item in words:

        # Remove the punctuation
        if (item == "." or item == ","): continue

        count += 1
    return count
