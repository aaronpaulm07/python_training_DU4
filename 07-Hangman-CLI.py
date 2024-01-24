def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

print("Hello")
word = 'watermelon'
point = 0
guess_count = 6
guessed_letters = []
print(display_word(word, guessed_letters))
print("Guess the word")

while guess_count > 0:
    current_guess = input().lower()

    if current_guess in guessed_letters:
        print("You already guessed that letter. Try others.")
        guess_count -= 1
    else:
        guessed_letters.append(current_guess)

        if current_guess in word:
            print("Good guess!")
        else:
            guess_count -= 1
            print(f"Incorrect guess! {guess_count} guesses left.")

        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You guessed the word!")
            break

if guess_count == 0:
    print(f"Game Over. The word was '{word}'.")
