# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "/Users/SCARLETT/Documents/learn_CS/MIT_CS/assignmnets/PS3/words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    #0. change the word in lowercase
    low_word = word.lower()
    #1.first_component
    first_component=0
    for i in range(len(word)):
        if low_word[i] != '*':
            first_component +=SCRABBLE_LETTER_VALUES[low_word[i]]
        i+=1
    #2.second_component
    cal_len = (7*len(word))-(3*(n-len(word)))
    if cal_len>1:
        second_component=cal_len
    else:
        second_component=1
    #3. return product
    return first_component * second_component

#
# Make sure you understand how this function works and what it does!
#
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print("Current hand:",end =' ')
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand={}
    num_vowels = int(math.ceil(n / 3))
    hand['*']=hand.get('*', 1)

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    #0.compare whether the letter in hand matches letter in word
    word=word.lower()
    new_hand=hand.copy()
    for letter in word:
        if letter in new_hand:

            #1. if matches illiminate the letter in hand
            if new_hand[letter] != 0:
                new_hand[letter] -= 1
    #2.return new hand
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    check_word = word.lower()
    check_hand=hand.copy()
    check_word_list=word_list
    check_2 =""

    for letter in check_word:
        if letter in check_hand:
            if check_hand[letter] != 0:
                check_hand[letter] -= 1
                check_2+=letter

    found=False
    if check_word in check_word_list:
        found = True
    elif check_word.find('*'):
        for vowel in VOWELS:
            changed_word = check_word.replace('*', vowel)
            if changed_word in check_word_list:
                found = True

    if check_2==check_word and found:
        return True
    else:
        return False
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    count_hand=0
    for letter in hand.keys():
        count_hand+=(hand[letter])
    return count_hand

def play_hand(hand, word_list):
    score = 0
    total_score=0
    while calculate_handlen(hand)!=0:
        display_hand(hand)
        word=str(input("Please enter a word or '!!' to indicate you are done:"))
        if word=="!!":
            break
        elif is_valid_word(word, hand, word_list)==True:
            score=get_word_score(word,calculate_handlen(hand))
            total_score += score
            print(word,"earned",score,"points. Total:", total_score, "points")
            new_hand = update_hand(hand,word)
            hand=new_hand
        else:
            print("That is not a valid word. Please choose another word.")

    print("Ran out of Letters")
    print("Total score for this hand:", total_score)
    print("----------------\n")
    return total_score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand):
    replace=False
    while replace == False:
        letter=str(input("Which letter would you like to replace:"))
        if letter in hand:
            alphabet=(VOWELS+CONSONANTS).replace(letter,"")
            x=random.choice(alphabet)
            hand['x']=hand[letter]
            del hand[letter]
            replace=True
        else:
            print("That letter is not in your hand.")
            replace=False


def play_game(word_list):
    total_num_hands=int(input("Enter total number of hands:"))
    overall_score=0
    replay =0
    #0.start of the game loop
    for i in range(total_num_hands):
        #1. setting up initial variables
        hand = deal_hand(HAND_SIZE)
        #1-1 print current hand
        display_hand(hand)
        print("Remaining number of hands:",total_num_hands)
        k=False
        while k==False:
            substitute=str(input("Would you like to substitute a letter?"))
            if substitute == "yes":
                hand=hand
                substitute_hand(hand)
                k=True
            elif substitute == "no":
                k=True
            else:
                print("you should enter either 'yes' or 'no'")
        if replay==0:
            play_hand(hand,word_list)
            #ask for replay
            rep_as=False
            while rep_as==False:
                rep=str(input("Would you like to replay hand?"))
                if rep=="yes":
                    replay=1
                    total=play_hand(hand,word_list)
                    overall_score+=total
                    rep_as=True
                elif rep =="no":
                    replay=0
                    rep_as=True
                else:
                    print("You should enter either 'yes' or 'no'")
        elif replay==1:
            total=play_hand(hand,word_list)
            overall_score+=total
        print("Total score for this hand:", total)
        print("Overall score up to now is", overall_score)
        total_num_hands-=1
    print("Total score over all hands:", overall_score)





#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
