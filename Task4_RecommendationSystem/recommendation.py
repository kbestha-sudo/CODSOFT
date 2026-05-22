movies = {
    "action": ["Avengers", "Batman", "John Wick"],
    "comedy": ["Mr Bean", "The Mask", "Jumanji"],
    "horror": ["Conjuring", "Nun", "Insidious"]
}

print("Movie Recommendation System")

genre = input("Enter genre: ").lower()

if genre in movies:
    print("Recommended Movies:")
    for movie in movies[genre]:
        print(movie)
else:
    print("Genre not found")
