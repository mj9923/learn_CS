WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_valid_word(word, hand, word_list):
    check_word = word.lower()
    check_hand=hand.copy()
    check_word_list=word_list
    print(check_word_list)
    check_2 =""
    for letter in check_word:
        if check_hand.has_key(letter):
            if check_hand[letter] != 0:
                check_hand[letter] -= 1
                check_2+=letter
    if check_2==check_word:
        for i in check_word_list:
            if i == word.lower():
                return True
            else:
                return False
    else:
        return False

if __name__ == '__main__':
    word_list = load_words()

#print(is_valid_word('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, word_list))
is_valid_word('hEllo', {'h': 1, 'e': 1, 'l': 2, 'o': 1}, word_list)

#print(is_valid_word('honey', {'e': 2, 'd': 1, 'h': 1, 'o': 1, 'n': 1, 'w': 1, 'y': 1}, word_list))

#print(is_valid_word('EVIL', {'i': 1, 'n': 1, 'e': 1, 'l': 2, 'v': 2}, word_list))
