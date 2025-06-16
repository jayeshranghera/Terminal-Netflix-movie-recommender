import pandas as pd

#  Load movie data
def load_movies(file_path):
    try:
        movies = pd.read_csv(file_path)
        print(" Movies loaded successfully!")
        print(movies.head())
        return movies
    except FileNotFoundError:
        print("File not found.")
        return None

#  Clean user input helper
def ask_input(prompt):
    return input(prompt).strip().lower()

#  Get preferences from user
def get_user_preferences():
    print("\n Let's find a movie for you!\n")

    mood = ask_input(" Mood (e.g., inspiring, emotional, feel-good): ")
    genre = ask_input(" Genre (e.g., drama, comedy, sci-fi, romance): ")

    print("⏱ Duration:\n  1. Short (<90 mins)\n  2. Medium (90–120 mins)\n  3. Long (>120 mins)")
    duration_map = {'1': 'short', '2': 'medium', '3': 'long'}
    duration = duration_map.get(ask_input(" Choose (1/2/3): "), 'medium')

    return mood, genre, duration

#  Filter and recommend movies
def recommend_movies(df, mood, genre, duration):
    df = df[
        (df['mood'].str.lower() == mood) &
        (df['genre'].str.lower() == genre)
    ]

    duration_filter = {
        'short': df['duration'] < 90,
        'medium': (df['duration'] >= 90) & (df['duration'] <= 120),
        'long': df['duration'] > 120
    }

    df = df[duration_filter.get(duration, True)]

    if df.empty:
        print("\n😕 No matches found. Try different filters.\n")
    else:
        print("\n Your Recommendations:\n")
        for _, row in df.iterrows():
            print(f"🎬 {row['title']} ({row['year']}) - {row['duration']} mins")

#  Main runner
if __name__ == "__main__":
    movies = load_movies("data/movies.csv")

    if movies is not None:
        mood, genre, duration = get_user_preferences()
        print(f"\n You Selected: {mood} | {genre} | {duration}")
        recommend_movies(movies, mood, genre, duration)
