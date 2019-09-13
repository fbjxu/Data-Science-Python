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
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALLLETTERS = VOWELS + CONSONANTS
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    #make sure all letters in word are lower case letters
    user_word = word.lower()
    first_comp = 0
    for elt in user_word:
        first_comp += SCRABBLE_LETTER_VALUES.get(elt, 0)
    sec_comp = max(7*len(user_word) - 3*(n-len(user_word)), 1)
    return first_comp * sec_comp




#
# Make sure you understand how this function works and what it does!
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

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

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
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n-1):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    hand['*'] = 1

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
    word_lower = word.lower()
    update_hand = copy.deepcopy(hand)
    for elt in word_lower:
        if elt in update_hand:
            update_hand[elt] = max(update_hand.get(elt) - 1,0)
            if update_hand[elt]==0: del(update_hand[elt])
    return update_hand

##test
#hand = {'a': 1, 'b': 2, 'c': 3}
#word = 'bccc'
#update_hand(hand,word)


#
# Problem #3: Test word validity
#


def is_in_hand(word, hand):
    word_lower= word.lower()
    word_freq = get_frequency_dict(word_lower)
    result = []
    for elt in word_freq.keys():
        if hand.get(elt, 0) >= word_freq[elt]:
            result.append(True)
        else:
            result.append(False)

    in_hand = (sum(result) == len(result))
    return in_hand


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #step 1: convert word to all lower-case letters
    word_lower = word.lower()
    #preliminary: check if user provided any wild card char
    if word_lower.find('*') != -1:
        possible_words = []

        #get all possible words with the wild card
        for vowel in VOWELS:
            guessed_word = word_lower.replace("*", vowel)
            possible_words.append(guessed_word)


        #check if any possible words could be found in the word list and met the hand requirement
        approved_words = []
        for word in possible_words:
            if (word in word_list) and is_in_hand(word_lower,hand):
                approved_words.append(word)


        if len(approved_words) <= 0: return False
        else: return True

    else:
    #step 2: check if the word exists in word_list
        in_word_list = (word_lower in word_list)
    #step 3: check if the word is entirely composed of letters in the hand
        return (in_word_list and is_in_hand(word_lower, hand))



# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    count = 0
    for elt in hand.keys():
        count += hand.get(elt, 0)
    return count

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    score = 0
    hand_provided = copy.deepcopy(hand)
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand_provided) > 0:
        remaining_letters = calculate_handlen(hand_provided)
        # Display the hand
        print('Current hand is: ')
        display_hand(hand_provided)
        # Ask user for input
        user_word = str(input('Enter word, or "!!" to indicate that you are finished: '))
        # If the input is two exclamation points:
        if user_word == "!!":
            print('You have decided to exit the game. Your total score is: ', score)
            return None
            # End the game (break out of the loop)


        # Otherwise (the input is not two exclamation points):
        else:
            if is_valid_word(user_word, hand_provided, word_list):
                score += get_word_score(user_word, remaining_letters)
                print('"', user_word, '"', 'earned', get_word_score(user_word, remaining_letters), 'pts! Your total score is:',
                      score, '!')

            # If the word is valid:
            else:
                print('That is not a valid word.')
            hand_provided = update_hand(hand_provided, user_word)

    print('Ran out of letters. Total score:', score, 'points')
    return score



#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    new_hand = copy.deepcopy(hand)

    options = list(ALLLETTERS)

    for e in options:
        if e in hand.keys():
            options.remove(e)

    sub_letter = random.choice(options)
    new_hand[sub_letter] = hand[letter]
    del(new_hand[letter])

    return new_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    *

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    #1 Asks the user to input a total number of hands
    hand_count = int(input("Enter total number of hands"))
    hand_size = int(input("How many cards would you like in one hand?"))
    game_record = []

    for play in range(hand_count):
        replay_record = []
        user_hand = deal_hand(hand_size)
        display_hand(user_hand)
        sub_response = input("Would you like to substitute a letter? Enter yes or no")
        if sub_response == 'yes':
            sub_letter = input('Which letter you would like to substitute?')
            sub_hand = substitute_hand(user_hand, sub_letter)
            hand_score = play_hand(sub_hand, word_list)
            replay_record.append(hand_score)
            #print(replay_record)

        else:
            hand_score = play_hand(user_hand, word_list)
            replay_record.append(hand_score)
#            print(hand_score)
#            print(replay_record)


        replay_response = input("Would you like to replay this hand? Enter yes or no")
        if replay_response == 'yes':
            hand_score = play_hand(user_hand, word_list)
            replay_record.append(hand_score)
#            print(hand_score)
#            print(replay_record)
        game_record.append(max(replay_record))
        game_score = sum(game_record)
        print('For this game, you scored:', game_score)





    #game_score = sum(score_record)
    #print("For this game, you scored:", game_score)
    return game_score


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
