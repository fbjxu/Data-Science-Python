# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
import copy
import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
valid_words = load_words(WORDLIST_FILENAME)
# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words =  valid_words
        
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        msg_text = self.message_text
        return msg_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_valid_words = copy.deepcopy(self.valid_words)
        return copy_valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        #step 1 create a dictionary that maps all consonant letters to themselves
        alphabet_map = {}
        for elt in CONSONANTS_LOWER:
            alphabet_map[elt] = elt
        for elt in CONSONANTS_UPPER:
            alphabet_map[elt] = elt
        alphabet_map['A'] = vowels_permutation[0].upper()
        alphabet_map['E'] = vowels_permutation[1].upper()
        alphabet_map['I'] = vowels_permutation[2].upper()
        alphabet_map['O'] = vowels_permutation[3].upper()
        alphabet_map['U'] = vowels_permutation[4].upper()
        alphabet_map['a'] = vowels_permutation[0].lower()
        alphabet_map['e'] = vowels_permutation[1].lower()
        alphabet_map['i'] = vowels_permutation[2].lower()
        alphabet_map['o'] = vowels_permutation[3].lower()
        alphabet_map['u'] = vowels_permutation[4].lower()
        return alphabet_map
        
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        transposed_text = ""
        msg_to_be_transposed = self.get_message_text()
        for char in msg_to_be_transposed:
            transposed_text += transpose_dict.get(char, char)
        
        return transposed_text
            
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #1 obtain all permutations for vowels
        encrypted_msg = self.get_message_text()
        #all_vowel_perm is a list encapsulating all possible permutations for vowels
        all_vowel_perm = get_permutations('aeiou')
        
        #2 for each permutation, obtain the msg and count the of valid words. Store the result
        #in a dictionary {# valid word: msg}
        possible_msg = {}
        for elt in all_vowel_perm:
            transpose_dict = self.build_transpose_dict(elt)
            msg = self.apply_transpose(transpose_dict)
            msg_words = msg.split()
            valid_cnt = 0
            for word in msg_words:
                if is_word(self.get_valid_words(), word):
                    valid_cnt += 1
            possible_msg[valid_cnt] = msg
        #3 
        max_valid_cnt = max(possible_msg.keys())
        if max_valid_cnt == 0:
            return encrypted_msg
        else:
            return possible_msg[max_valid_cnt]
        
if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    message_two = SubMessage('Who do you think you are?')
    permutation = 'uaioe'
    enc_dict = message_two.build_transpose_dict(permutation)
    print('Original message:', message_two.get_message_text(), 'Permutation:', permutation)
    print('Expectected Encryption:', 'Who do yoe think yoe ura?')
    print('Actual encryption:', message_two.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message_two.apply_transpose(enc_dict))
    print('Decrypted message:', enc_message.decrypt_message())
