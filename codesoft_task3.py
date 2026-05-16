
movies = {
    "action": [
        "Dhurandar",
        "War",
        "KGF",
        "Vikram",
        "Bang Bang"
    ],
    "comedy": [
        "GOlmaal",
        "3 Idiots",
        "Deadpool",
        "Jumanji",
        "hera pheri"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "IT",
        "Annabelle",
        "The Nun"
    ],
    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "A Walk to Remember",
        "Before Sunrise"
    ],
    "science fiction": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar",
        "Doctor Strange"
    ],
}
def recommend_movies():
    print("   MOVIE RECOMMENDATION SYSTEM")
    
    print("\nAvailable Categories:\n")

    for category in movies:
        print("👉", category.title())

    while True:
        user_choice = input(
            "\nEnter movie category (or type 'exit'): "
        ).lower()

       
        if user_choice == "exit":
            print("\n👋 Thank you for using the system!")
            break

       
        elif user_choice in movies:

            print(f"\n🎬 Recommended {user_choice.title()} Movies:\n")
    
            for movie in movies[user_choice]:
                print("⭐", movie)
        else:
            print("\n❌ Category not found!")
            print("Please choose a valid category.")
recommend_movies()
