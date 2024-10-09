import random

def hangman():
    
    words = ["jpython", "java", "javascript", "hangman", "programming", "code", "developer", "computer"]
    word = random.choice(words).lower()  
    guessed_word = ["_" for _ in word]  
    attempts = 6  # Number of attempts allowed
    guessed_letters = []  # List to store guessed letters

    print("Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess: ", " ".join(guessed_word))
        else:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"You've run out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
