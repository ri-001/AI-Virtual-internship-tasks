movies = {
    "Avengers": ["Action", "Sci-Fi"],
    "Iron Man": ["Action", "Sci-Fi"],
    "Batman": ["Action"],
    "John Wick": ["Action", "Thriller"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance"],
    "La La Land": ["Romance", "Musical"],
    "Conjuring": ["Horror"],
    "Insidious": ["Horror"],
    "Annabelle": ["Horror"],
    "Interstellar": ["Sci-Fi"],
    "Inception": ["Sci-Fi", "Thriller"],
    "The Dark Knight": ["Action", "Thriller"]
}

user_ratings = {}

print(" MOVIE RECOMMENDATION SYSTEM")
print("\nAvailable Movies:\n")

for movie in movies:
    print("-", movie)

print("\nRate the movies you have watched.")
print("Rating Scale: 1 to 5")
print("Enter 0 if not watched.\n")

for movie in movies:
    rating = int(input(f"Rate '{movie}': "))

    if rating > 0:
        user_ratings[movie] = rating

genre_scores = {}

for movie, rating in user_ratings.items():

    genres = movies[movie]

    for genre in genres:

        if genre not in genre_scores:
            genre_scores[genre] = 0

        genre_scores[genre] += rating

print("\nYour Genre Preferences:")
for genre, score in genre_scores.items():
    print(f"{genre} : {score}")

recommendations = {}

for movie in movies:
    if movie in user_ratings:
        continue
    score = 0
    for genre in movies[movie]:

        if genre in genre_scores:
            score += genre_scores[genre]
    recommendations[movie] = score

sorted_recommendations = sorted(
    recommendations.items(),
    key=lambda x: x[1],
    reverse=True
)

print("TOP RECOMMENDATIONS")
for movie, score in sorted_recommendations[:5]:
    print(f"{movie}  --> Recommendation Score: {score}")

    
