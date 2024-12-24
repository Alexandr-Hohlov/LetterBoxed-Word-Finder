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