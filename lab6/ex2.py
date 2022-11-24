import re
from ex1 import extract_words

def match_words(regex, text, x):
    words = extract_words(text)
    matches = []
    for word in words:
        if re.match(regex, word) and len(word) == x:
            matches.append(word)
    return matches


def main():
    words = match_words(r'[abcd]', 'Ana are mere', 3)
    print(words)

main()