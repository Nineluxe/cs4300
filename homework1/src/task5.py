
def printFirstThreeFavs():
    combinedAuthors = ["Stephen King", "IT", "Ira Levin", "Rosemary's Baby", "Michael Graziano", "The Divine Farce"]
    favoriteBooks = combinedAuthors[1:6:2]
    for i in favoriteBooks:
        print(i, end=" ")

def createStudentDatabase():
    return {
        "Bryce": "001",
        "Alex": "002",
        "Elijah": "003"
    }

