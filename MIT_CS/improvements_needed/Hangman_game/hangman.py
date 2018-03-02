
# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter == letters_guessed[0]:
            return True
    return False



def get_guessed_word(secret_word, letters_guessed):
    guessed_word=""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word = guessed_word + letter
        else:
            guessed_word = guessed_word + "_"
    return guessed_word


def get_available_letters(letters_guessed):
    remaining_letters="abcdefghijklmnopqrstuvwxyz"
    for letter in remaining_letters:
        if letter in letters_guessed:
            #strikeout guessed letter
            remaining_letters = remaining_letters.replace(letter,'\u0336'.join(letter) + '\u0336')
    return remaining_letters

def warnings_count(warnings, guesses):
    if warnings==0:
        guesses -= 1
        print("You have no warnings left. So you will lose one guess.\nYou have",guesses,"guesses left.")
    elif warnings==1:
        warnings-=1
        print("You have no warnings left. You will lose guesses from now on")
    else:
        warnings-=1
        print("You have",warnings,"warnings left.")
    
def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses=6
    warnings=3
    letters_guessed=[]

    while guesses > 0:
        #show number of warnings
        print("You have",warnings,"warnings left.")

        #show number of guesses
        if guesses==1:
            print ("This is your last guess")
        else:
            print("You have",guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))


        #Making a guess
        guess = False
        while guess == False:
            entered_letter = str.lower(input("Guess one letter!\n"))
            if str.isalpha(entered_letter)==True :
                if len(entered_letter)==1:
                    if entered_letter not in letters_guessed:
                        letters_guessed.insert(0, entered_letter)
                        find=True
                        break
                    else:
                        print("\nYou have already guessed that letter, try a different one! \n")
                else:
                    print("You should only guess one letter at a time.")
            else:
                print("You should write a letter")
            warnings_count(warnings, guesses)

        if is_word_guessed(secret_word, letters_guessed) == False:
            print("Your guess is wrong, better luck next time.")
            vowels=['a','e','i','o','u']

            wrong_vowel=False
            for letter in vowels:
                if entered_letter==letter:
                    wrong_vowel=True

            if wrong_vowel==True:
                guesses-=1
            else:
                guesses-=2
        else:
            print("Your guess is correct!")
        my_word=get_guessed_word(secret_word, letters_guessed)
        print(my_word)
        print("Your guesses were:", letters_guessed, "\n-----------------")


        if my_word == secret_word:
            print("\nHurray! You have won!")
            total_score=gueses*len(secret_word)
            print("Your tatal score for this game is:",total_score)
            break

    print("\nBoo you lost...\n\n My word was", secret_word)
    total_score=0
    print("Your tatal score for this game is:",total_score)

def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ','')
    other_word = other_word.replace(' ','')
    if len(my_word) != len(other_word):
        return False
    
    my_word_list = list(my_word)
    other_word_list = list(other_word)
    i = 0
    for letter in my_word_list:
        if letter != '_':
            if my_word_list.count(letter) != other_word_list.count(letter):
                return False
            if letter != other_word_list[i]:
                return False
        i += 1
    return True

def show_possible_matches(my_word):
    matches = False
    match_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_list.append(word)
            matches = True
    if matches:
        print("Possible word matches are:")
        print(' '.join(match_list))
    else:
        print("No matches found")

def hangman_with_hints(secret_word):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    guesses=6
    warnings=3
    letters_guessed=[]

    while guesses > 0:
        #show number of warnings
        print("You have",warnings,"warnings left.")

        #show number of guesses
        if guesses==1:
            print ("This is your last guess")
        else:
            print("You have",guesses,"guesses left.")
        print("Available letters:",get_available_letters(letters_guessed))


        #Making a guess
        guess = False
        while guess == False:
            entered_letter = str.lower(input("Guess one letter!\n"))
            if str.isalpha(entered_letter)==True :
                if len(entered_letter)==1:
                    if entered_letter not in letters_guessed:
                        letters_guessed.insert(0, entered_letter)
                        find=True
                        break
                    else:
                        print("\nYou have already guessed that letter, try a different one! \n")
                else:
                    print("You should only guess one letter at a time.")
            elif entered_letter=="*":
                show_possible_matches(my_word)
            else:
                print("You should write a letter")
            warnings_count(warnings, guesses)

        if is_word_guessed(secret_word, letters_guessed) == False:
            print("Your guess is wrong, better luck next time.")
            vowels=['a','e','i','o','u']

            wrong_vowel=False
            for letter in vowels:
                if entered_letter==letter:
                    wrong_vowel=True

            if wrong_vowel==True:
                guesses-=1
            else:
                guesses-=2
        else:
            print("Your guess is correct!")
        my_word=get_guessed_word(secret_word, letters_guessed)
        print(my_word)
        print("Your guesses were:", letters_guessed, "\n-----------------")


        if my_word == secret_word:
            print("\nHurray! You have won!")
            total_score=gueses*len(secret_word)
            print("Your tatal score for this game is:",total_score)
            break

    print("\nBoo you lost...\n\n My word was", secret_word)
    total_score=0
    print("Your tatal score for this game is:",total_score)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
