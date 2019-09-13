#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:08:18 2019

@author: lazybear
"""

#towers of hanoi
def print_move(fr, to):
    print('move from', str(fr), 'to', str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


Towers(5, 'a', 'b', 'c')

x = input("what is this input?")
print(x)
#fibonacci numbers
def fib(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

fib(5)

#palindrome
def is_palindrome(s):
    '''
    s: a string provided by user
    this function returns true if the string provided by user is a palindrome; False otherwise.
    '''

    def to_char(s):
        '''s: an input provided by user
        this function converts the user input to lower-case letters
        '''
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans += c
        return ans

    def is_pal(s):
        '''s: word that needs to be tested for palindrome
        '''
        if len(s) == 0 or len(s) == 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_char(s))

is_palindrome('asa')


#dictionary
grades = {'Anna': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
grades['Sylvan'] = 'C'
'Anna' in grades
del(grades['Anna'])
grades['Anna']

grades.keys()
grades.values()



#functions to analyze song lyrics:

def lyrics_to_frequency(lyrics):
    '''
    lyrics: list of words found in a specific song
    return a dictionary such that {'word': times}
    '''
    freq = {}
    for e in lyrics:
        if e in freq:
            freq[e] += 1
        else:
            freq[e] = 1
    return freq

def most_common_words(freq):
    '''
    freq: a dictionary object of the format {'word': times} for a specific song
    returns a tuple (list, int) that shows the word(s) that show up the most in the song along with
    the frequency
    '''
    popular_word = []
    times = freq.values()
    best = max(times)
    for e in freq.keys():
        if freq[e] == best:
            popular_word.append(e)
    return (popular_word, best)



def words_often(freq, minTimes):
    '''
    freq: a dictionary object of the format {'word': times} for a specific song
    minTimes: the minimum times certain word(s) show up in the song
    returns a list of tuples of the format (list, int) that shows the words that shows up at least
    x amount of times. x is determined by minTimes
    '''
    done = False
    result = []
    while not done:
        current_most_popular = most_common_words(freq)
        if current_most_popular[1] >= minTimes:
            result.append(current_most_popular)
            for w in current_most_popular[0]:
                del(freq[w])
        else:
            done = True
    return result


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah',
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = she_loves_you

words_often(beatles, 5)

#memoization: Fibonacci with a dicionary
def fib_efficient(n,d):
    '''
    n: is the n for fib(n)
    d: a dictionary that store intermediary results
    '''
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {0:1, 1:1} #initate base case

fib_efficient(5,d)
