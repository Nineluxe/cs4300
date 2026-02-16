
def printFirstThreeFavs():
    """ Prints the first three favorite books titles. """
    combinedAuthors = ["Stephen King", "IT", "Ira Levin", "Rosemary's Baby", "Michael Graziano", "The Divine Farce"]
    
    # Creates a list of only the book titles
    favoriteBooks = combinedAuthors[1:6:2]
    for i in favoriteBooks:
        print(i, end=" ")

# Returns a dictionary of student names and IDs
def createStudentDatabase():
    """ Returns a dictionary of student names and ID pairs. """
    return {
        "Bryce": "001",
        "Alex": "002",
        "Elijah": "003"
    }

