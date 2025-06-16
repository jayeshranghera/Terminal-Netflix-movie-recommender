# Terminal-Netflix-movie-recommender

#  Terminal Netflix — Movie Recommender

A simple, terminal-based movie recommender built using **Python and Pandas**, with zero machine learning — just clean logic and user-driven filters!

---

##  Features

-  Recommend movies based on **mood**, **genre**, and **duration**
-  Command-line based interaction
-  Logic-based filtering (No ML used!)
-  Loads movie data from CSV file
-  Simple, clean, beginner-friendly Python code

---

##  How it Works

Load Movie Data - 
The program loads movie information from a CSV file (movies.csv) which contains:

Title,Genre,Mood,Duration,Release Year

Take User Input - 
The user is asked three simple questions:

Mood → e.g., inspiring, feel-good, emotional

Genre → e.g., drama, comedy, sci-fi

Duration Preference → Short (<90 mins), Medium (90–120 mins), Long (>120 mins)

Filter Movies - 
Based on the inputs, the program filters the movies using simple logic (no machine learning involved) by:

Matching the mood (case-insensitive)

Matching the genre

Categorizing duration into short, medium, or long based on runtime

Show Recommendations

If matches are found, a list of suitable movies is displayed.

If no matches are found, it politely informs the user and ends the program.

Exit - 
The program ends after showing recommendations — clean and minimal.



