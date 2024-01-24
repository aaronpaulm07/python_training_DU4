import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Suppress only the InsecureRequestWarning from urllib3 needed for this example
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def get_random_word():
    api_url = "https://random-word-api.herokuapp.com/word"
    
    try:
        # Make a GET request to the API
        response = requests.get(api_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the word from the response
            word = response.json()[0]
            return word
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# random_word = get_random_word()
# print("Random word:", random_word)

print("Hello")
word = get_random_word()
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
