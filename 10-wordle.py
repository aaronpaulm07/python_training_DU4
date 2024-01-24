import random

def choose_word():
    word_list = ["apple", "banana", "orange", "kiwi", "peach"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def wordle():
    selected_word = choose_word()
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Wordle!")
    print("Try to guess the hidden word.")

    while attempts_left > 0:
        current_display = display_word(selected_word, guessed_letters)
        print(current_display)
        guess = input("Enter your guess: ").lower()

        if guess == selected_word:
            print(f"Congratulations! You guessed the word: {selected_word}")
            break
        if guess in selected_word:
            guessed_letters.add(guess)

            if set(selected_word).issubset(guessed_letters):
                print(f"Congratulations! You guessed the word: {selected_word}")
                break
        else :
            attempts_left -= 1
            print(f"Incorrect guess! {attempts_left} attempts left.")

    if attempts_left == 0:
        print(f"Game Over. The word was: {selected_word}")

if __name__ == "__main__":
    wordle()
