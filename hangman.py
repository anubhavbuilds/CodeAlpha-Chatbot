import random
def play_hangman():
    # List of predefined words
    categories={
        "Fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "orange"],
        "Animals": ["elephant", "giraffe", "kangaroo", "lion", "monkey", "penguin", "rabbit", "tiger", "zebra"],
        "Countries": ["argentina", "brazil", "canada", "denmark", "egypt", "france", "germany", "hungary", "india", "japan"],
        "Colors": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"],
        "Sports": ["soccer", "basketball", "tennis", "cricket   ", "baseball", "hockey", "golf", "swimming", "cycling", "volleyball"],
        "Programming":["python", "java", "javascript", "csharp", "ruby", "php", "swift", "kotlin", "typescript", "go"]
    }

    # Select a random category
    category = random.choice(list(categories.keys()))
    print(f"Category: {category}")

    # Select a random word from the chosen category
    word = random.choice(categories[category])

    # Create a list of underscores
    guessed_word = ["_"] * len(word)

    # Store guessed letters
    guessed_letters = []

    # Maximum wrong attempts
    attempts = 6
   
    print("====== WELCOME TO HANGMAN GAME ======")

    print("🎮 Choose a category: ")
    print("1. Fruits")
    print("2. Animals")
    print("3. Countries")
    print("4. Colors")
    print("5. Sports")
    print("6. Programming")
    option=input("Enter your choice (1-6): ")
    if option=="1":
        category="Fruits"
        for fruit in categories[category]:
            word = random.choice(categories[category])
    elif option=="2":
        category="Animals"
        for animal in categories[category]:
                 word = random.choice(categories[category])
    elif option=="3":
        category="Countries"
        for country in categories[category]:
                word = random.choice(categories[category])
    elif option=="4":
        category="Colors"
        for color in categories[category]:
            word = random.choice(categories[category])
    elif option=="5":
        category="Sports"
        for sport in categories[category]:
            word = random.choice(categories[category])  
    elif option=="6":
        category="Programming"
        for programming in categories[category]:
            word = random.choice(categories[category])
    else:
        print("❌ Invalid choice. Defaulting to random category.")

    while attempts > 0 and "_" in guessed_word:
        print("Word: ", " ".join(guessed_word))
        print("❤️ Lives Left:", attempts)
        print("Guessed Letters:", guessed_letters)

        guess = input("🔤 Enter a letter: ").lower()

        # Check if user enters only one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed this letter.")
            continue

        guessed_letters.append(guess)

        # Check if letter is in word
        if guess in word:
            print("Correct Guess!")

            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess

        else:
            print("❌ Wrong Guess!")
            attempts -= 1

    # Final Result
    print("\n==============================")

    if "_" not in guessed_word:
        print("🏆 Congratulations! You Won!")
        print("Word was:", word)
    else:
        print("☠️ Game Over!")
        print("😁 The correct word was:", word)

    print("==============================")
pass
while True:
    play_hangman()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing! ☺️ Goodbye!")
        break