import re

rgx = "^L.*[AB].*$"

with open("output.txt", "r") as f:
    for word in f.readlines():
        m = re.search(rgx, word)

        if m and m.group() == word.rstrip():
            print(word.rstrip())