# Define the movie data
movies = {
    'movie1': {'genre': 'action', 'director': 'Director A', 'year': 2010, 'rating': 7.5},
    'movie2': {'genre': 'drama', 'director': 'Director B', 'year': 2015, 'rating': 8.2},
    'movie3': {'genre': 'comedy', 'director': 'Director C', 'year': 2012, 'rating': 6.8},
    'movie4': {'genre': 'horror', 'director': 'Director D', 'year': 2017, 'rating': 6.5},
    'movie5': {'genre': 'romance', 'director': 'Director E', 'year': 2014, 'rating': 7.9},
    'movie6': {'genre': 'thriller', 'director': 'Director F', 'year': 2011, 'rating': 7.1},
    'movie7': {'genre': 'sci-fi', 'director': 'Director G', 'year': 2016, 'rating': 8.0},
    'movie8': {'genre': 'animation', 'director': 'Director H', 'year': 2013, 'rating': 7.3},
    'movie9': {'genre': 'adventure', 'director': 'Director I', 'year': 2009, 'rating': 7.7},
    'movie10': {'genre': 'fantasy', 'director': 'Director J', 'year': 2018, 'rating': 7.4}
}

def recommend_movies(user_preferences, movies):
    recommended_movies = []
    
    for movie_id, details in movies.items():
        # Filter based on genre preference
        if details['genre'] == user_preferences['genre']:
            recommended_movies.append((movie_id, details))
    
    # Sort recommended movies by closeness to preferred rating and year
    recommended_movies.sort(key=lambda x: (abs(x[1]['rating'] - user_preferences['rating']), abs(x[1]['year'] - user_preferences['year'])))
    
    return recommended_movies

# Function to get user preferences for movies
def get_user_preferences():
    print("Welcome to the Movie Recommendation System!")
    print("Please enter your preferences:")
    user_preferences = {}
    user_preferences['genre'] = input("Genre of movie (e.g., action, drama, comedy): ").strip().lower()
    user_preferences['year'] = int(input("Preferred release year of movie: "))
    user_preferences['rating'] = float(input("Preferred rating you prefer (out of 10): "))
    return user_preferences

# Main function to run the recommendation system
def main():
    user_preferences = get_user_preferences()
    recommended_movies = recommend_movies(user_preferences, movies)
    
    # Display recommended movies or message if no movies match
    if recommended_movies:
        print("\nRecommended Movies:")
        for movie_id, details in recommended_movies:
            print(f"Movie ID: {movie_id}, Genre: {details['genre']}, Director: {details['director']}, Year: {details['year']}, Rating: {details['rating']}")
    else:
        print("\nSorry, no movies match your preferences.")

if __name__ == "__main__":
    main()
