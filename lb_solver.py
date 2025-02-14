
"""

Letter Boxed is a game where you make words out of a square with 3 letters on each side (I don't think any repeat).

The goal is to chain 4-6 words together (end letter of word 1 is start letter of word 2) such that each letter in the square is used at least once.

The rule is that once you've chosen a letter on one side of the square, your next letter can't be on that same side, it must be on one of the 3 sides.



Ex:

  T   R   N
F           E

H           I

M           P
  S   B   A

  
There might also be a letter limit (4 letters minimum?)
THIN is a valid word
PIE is NOT a valid word (Uses consecutive letters from the same side)


- Will a Regex work for solving this?
- Maybe a bunch of regexes?  


Good strategies?
-> Getting difficult letters earlier? (Humans)
-> Finding the biggest word first?

Programming Strategies?
-> Go down each word in the dictionary that contains only these letters and see if it is possible to create that word with this square
  
Example:
From S1 - T
From S2 - H
From S3 - I
From S1 - N

Algorithms for solving the whole box:
- Always pick the word that uses the most unique letters (out of the letters that are left)

- Pick 2 words that use up all the letters between them, then find a connecting word between those 2
-> Might not always be possible? Might need 3 words that use up all the letters

- Some kind of Brute force algorithm


Really good strategy perhaps?
-> See if there is one word that uses all 12 letters
-> See if there are two words that use all 12 letters
-> see if there are three words that use all 12 letters
-> Ideally the words should be connected?


Make it work as a Command Line Utility:

py lb_solver.py abc def ghi jkl
^
Something like that
-> Will try to solve in 2 words, then 3, then 4, and etc...
-> If slow, try multithreading?
   -> Maybe try it anyway?

"""

import sys

def find_connected_words(file: str):
    wordlist = []
    # Return a list of solutions instead of print???
    solutions = []
    solved = 0

    with open(file, "r") as f:
        wordlist = f.readlines()

    print("------- 1 Word Solutions -------")
    for w1 in wordlist:
        if len(set(w1.rstrip())) == 12:
            print(w1.rstrip())
            solved = 1

    print("------- 2 Word Solutions -------")
    for w1 in wordlist:
        for w2 in wordlist:
            if w1.rstrip()[-1] == w2.rstrip()[0] and len(set(w1.rstrip() + w2.rstrip())) == 12:
                print(w1.rstrip() + "  " + w2.rstrip())
                solved = 1
    
    if solved == 0:
        print("------- 3 Word Solutions -------")
        for w1 in wordlist:
            for w2 in wordlist:
                for w3 in wordlist:
                    first_connection = w1.rstrip()[-1] == w2.rstrip()[0]
                    second_connection = w2.rstrip()[-1] == w3.rstrip()[0]
                    if first_connection and second_connection and len(set(w1.rstrip() + w2.rstrip() + w3.rstrip())) == 12:
                        print(w1.rstrip() + "  " + w2.rstrip() + "  " + w3.rstrip())
                        solved = 1

# Maybe output a list of words if there are ties
def find_most_unique_letters(file: str):
    most_unique_letters = 0
    current_words = []
    with open(file, "r") as f:
        for word in f.readlines():
            num_unique = len(set(word))

            if num_unique > most_unique_letters:
                current_words  = [word.rstrip()]
                most_unique_letters = num_unique

            elif num_unique == most_unique_letters:
                current_words.append(word.rstrip())
    
    return current_words

output = "output.txt"

# This probably works???
# s0 = ['TRN']
# s1 = ['FHM']
# s2 = ['EIP']
# s3 = ['SBA']


# Command Line Arguments:
# py lb_solver.py abc def ghi jkl

if len(sys.argv) == 5:
    s0 = sys.argv[1].upper()
    s1 = sys.argv[2].upper()
    s2 = sys.argv[3].upper()
    s3 = sys.argv[4].upper()

else:
    s0 = "ZMC"
    s1 = "GHA"
    s2 = "NTI"
    s3 = "SRO"

#s0 = ['G', 'N', 'A']
#s1 = ['I', 'Y', 'J']
#s2 = ['R', 'K', 'P']
#s3 = ['O', 'C', 'T']

box = [s0, s1, s2, s3]
box_flat = s0 + s1 + s2 + s3

final_list = []

# Go through the dictionary and find words that can be made with letterboxed rules

with open("scrabble_dictionary.txt", "r") as f:
    for word in f.readlines():
        w = word.rstrip()
        last_side = -1
        c_i = 0
        valid_word = True

        while c_i < len(w) and valid_word == True:
            
            # TODO: Make this better
            if w[c_i] in s0 and last_side != 0:
                last_side = 0
            elif w[c_i] in s1 and last_side != 1:
                last_side = 1
            elif w[c_i] in s2 and last_side != 2:
                last_side = 2
            elif w[c_i] in s3 and last_side != 3:
                last_side = 3
            else:
                valid_word = False

            c_i += 1
        
        if valid_word == True:
            final_list.append(w + "\n")

with open(output, "w") as f:
    f.writelines(sorted(final_list, key=len))

print("words with most unique letters:")
for x in find_most_unique_letters(output):
    print(x)

find_connected_words(output)

