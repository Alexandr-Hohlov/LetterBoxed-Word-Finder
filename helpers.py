"""
Various helper functions for the game

"""

output = "output.txt"


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


print("words with most unique letters:")
for x in find_most_unique_letters(output):
    print(x)

# Maybe after this, update output.txt with a new list that contains words with the remaining letters, then:
# find the one that uses the most unique remaining letters.


"""
For each word in output.txt
If that word + a connected word take up all 12 unique letters - Print them?



"""

print("------- 2 Word Solutions -------")
def find_connected_words(file: str):
    wordlist = []
    solutions = []
    
    with open(file, "r") as f:
        wordlist = f.readlines()

    for w1 in wordlist:
        for w2 in wordlist:
            if len(set(w1.rstrip() + w2.rstrip())) == 12 and w1.rstrip()[-1] == w2.rstrip()[0]:
                print(w1.rstrip() + "  " + w2.rstrip())
    return solutions

find_connected_words(output)