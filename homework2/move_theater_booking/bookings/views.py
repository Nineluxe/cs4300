from django.shortcuts import render

# Create your views here.
def moviesListTest(request):
    movies = []

    # Open the file
    with open("movies.txt", "r") as file:
        for line in file:

            # Split the data inside the file
            title, director, year, duration = line.strip().split("|")

            # Create the structured data "packet"
            movies.append(
                {
                    "title": title,
                    "director": director,
                    "year": year,
                    "duration": duration
                }
            )

    # Pass the data to a template
    # Simulates what a database query would normally return
    return render(request, "bookings/moviesList.html", {"movies": movies})