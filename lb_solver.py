
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
"""

# This probably works???
# s0 = ['TRN']
# s1 = ['FHM']
# s2 = ['EIP']
# s3 = ['SBA']

s0 = ['T', 'R', 'N']
s1 = ['F', 'H', 'M']
s2 = ['E', 'I', 'P']
s3 = ['S', 'B', 'A']

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

with open("output.txt", "r+") as f:
    f.writelines(sorted(final_list, key=len))
    

          

