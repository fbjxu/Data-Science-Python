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
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word_list = list(secret_word)
    s_copy = secret_word_list[:]
    for e in secret_word_list:
        if e in letters_guessed:
            s_copy.remove(e)
    if len(s_copy) == 0:
        result = True
    else:
        result = False
    return result




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    #ensure both secret_word and letters_geussed are in lower cases
    secret_word_list = list(secret_word.lower())
    lower_letters_guessed = [x.lower() for x in letters_guessed]
    output = []
    for e in secret_word_list:
        if e in lower_letters_guessed:
            output.append(e)
        else:
            output.append('_ ')
    string_output = ''.join(output)
    return string_output

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet)
    alpha_copy = alphabet_list[:]
    for e in alphabet_list:
        if e in letters_guessed:
            alpha_copy.remove(e)
    available_letters = ''.join(sorted(alpha_copy))
    return 'Available letters: ' + available_letters



#self-defined function

def is_letter_in_word(secret_word, letter):
    '''
    secret_word: string, the secret word to guess
    letter: string
    returns true if the letter could be found in the secret_word; false otherwise
    '''
    if letter in secret_word:
        return True
    else:
        return False



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman, I am thinking of a word that is', len(secret_word), 'words long!\n', '--------\n')
    #initializing number of guesses
    num_guesses = 6
    warning = 3
    
    #initialize letters guessed by the user
    letters_guessed=[]
    
    while (num_guesses > 0 and warning >= 0 and is_word_guessed(secret_word, letters_guessed) == False):
        
        print('You have {} guesses left\n'.format(num_guesses))
        print(get_available_letters(letters_guessed))
    
        
        user_guess = input('Please guess a letter: ').lower()

        #case 1: user provided a valid letter
        if user_guess.isalpha() and len(user_guess) == 1:
        
            #case 1a: the letter provided by user has been guessed before 
            if user_guess in letters_guessed:
                #case 1a1: there are warning left
                if warning >0:
                    warning -=1
                    print('Oops! You have entered this letter before. You have {} warnings left:\n'.format(warning))
                #case 1a2: there are no warning left 
                else:
                    num_guesses -= 1
                    print('Oops! You have entered this letter before. You have {} warnings left\n'.format(warning), 'So you lose one guess:')
                    
            #case 1b: the letter provided by user has not been guessed before
            if  user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                #case 1b1: the letter could be found in the secret word
                if is_letter_in_word(secret_word, user_guess):
                    print('Good Guess! : \n')
                #case 1b2:the letter could not be found in the secret word
                else:
                    print('Oops! That letter is not in my word:\n')
                    num_guesses -=1

        #case 2: user did not provide a valid input
        else:
            warning -= 1
            print('Oops! That is not a valid letter. You have {} warnings left:\n'.format(warning))
                
        print(get_guessed_word(secret_word, letters_guessed))
        print('\n---------------------')
        
    #user got it right
    if is_word_guessed(secret_word, letters_guessed):
        print('You got it!')
        points = num_guesses * len(secret_word)
        print('You have received', points, 'points!')
    #user used all warnings 
    elif warning < 0:
        print('You used all warnings')
        print('The secret word that I have is:', secret_word)
    elif num_guesses <= 0:
        print('Sorry you ran out of guesses')
        print('The secret word that I have is:', secret_word)
  
        
hangman('tact')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    stripped_my_word = my_word.replace(' ', '')
    count = 0
    if len(stripped_my_word) != len(other_word):
        return False
    else:
        for i in range(len(stripped_my_word)):
            if stripped_my_word[i] == other_word[i] or stripped_my_word[i] == '_':
                count += 1
        if len(stripped_my_word) == count:
            return True
        else:
            return False
            
#my_word = 't_ t'
#other_word = 'tact'
#match_with_gaps(my_word, other_word)


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for e in wordlist:
        if match_with_gaps(my_word, e):
            possible_matches.append(e)
    if len(possible_matches)>0:
        print(possible_matches)
    else:
        print('No Matches Found')

my_word = 't_ _ t'
show_possible_matches(my_word)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman, I am thinking of a word that is', len(secret_word), 'words long!\n', '--------\n')
    #initializing number of guesses
    num_guesses = 6
    warning = 3
    
    #initialize letters guessed by the user
    letters_guessed=[]
    
    while (num_guesses > 0 and warning >= 0 and is_word_guessed(secret_word, letters_guessed) == False):
        
        print('You have {} guesses left\n'.format(num_guesses))
        print(get_available_letters(letters_guessed))
    
        
        user_guess = input('Please guess a letter: ').lower()
        

        #case 1: user provided a valid letter
        if user_guess.isalpha() and len(user_guess) == 1:
        
            #case 1a: the letter provided by user has been guessed before 
            if user_guess in letters_guessed:
                #case 1a1: there are warning left
                if warning >0:
                    warning -=1
                    print('Oops! You have entered this letter before. You have {} warnings left:\n'.format(warning))
                #case 1a2: there are no warning left 
                else:
                    num_guesses -= 1
                    print('Oops! You have entered this letter before. You have {} warnings left\n'.format(warning), 'So you lose one guess:')
                    
            #case 1b: the letter provided by user has not been guessed before
            if  user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                #case 1b1: the letter could be found in the secret word
                if is_letter_in_word(secret_word, user_guess):
                    print('Good Guess! : \n')
                #case 1b2:the letter could not be found in the secret word
                else:
                    print('Oops! That letter is not in my word:\n')
                    num_guesses -=1
        #special case
        elif user_guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))


        #case 2: user did not provide a valid input
        else:
            warning -= 1
            print('Oops! That is not a valid letter. You have {} warnings left:\n'.format(warning))
                
        print(get_guessed_word(secret_word, letters_guessed))
        print('\n---------------------')
        
    #user got it right
    if is_word_guessed(secret_word, letters_guessed):
        print('You got it!')
        points = num_guesses * len(secret_word)
        print('You have received', points, 'points!')
    #user used all warnings 
    elif warning < 0:
        print('You used all warnings')
        print('The secret word that I have is:', secret_word)
    elif num_guesses <= 0:
        print('Sorry you ran out of guesses')
        print('The secret word that I have is:', secret_word)
  

hangman_with_hints('tact')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
