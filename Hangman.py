import random
print("""H A N G M A N""")
list_of_words = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(list_of_words)
hidden_word = '-' * len(chosen_word)
letters_in_chosen_word = set(chosen_word)
guessed_letters = set()
lives = 8
print()
start_word = input('Type "play" to play the game, "exit" to quit: ')
if start_word == "play":
    print()
    print(hidden_word)
    while lives > 0:
        input_letter = input("Input a letter: ")
        if len(input_letter) != 1:
            print("You should input a single letter")
            print()
            print(hidden_word)
        elif not input_letter.isascii() or not input_letter.islower():
            print("Please enter a lowercase English letter")
            print()
            print(hidden_word)
        elif input_letter in hidden_word:
            print("You've already guessed this letter")
            print()
            print(hidden_word)
        elif input_letter in guessed_letters:
            print("You've already guessed this letter")
            print()
            print(hidden_word)
        elif input_letter not in chosen_word:
            guessed_letters.update(input_letter)
            print("That letter doesn't appear in the word")
            lives -= 1
            if lives == 0:
                print("You lost!")
                break
            print()
            print(hidden_word)
        elif input_letter in letters_in_chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == input_letter:
                    hidden_word = hidden_word[:i] + input_letter + hidden_word[i+1:]
            if hidden_word == chosen_word:
                print(f"""You guessed the word {chosen_word}!
You survived!""")
                break
            print()
            print(hidden_word)
