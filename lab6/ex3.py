import re
from ex1 import extract_words

def match_expressions(text, regex_list):
    words = extract_words(text)
    matches = []

    for word in words:
        for regex in regex_list:
            if re.match(regex, word):
                matches.append(word)
                break
    return matches

def main():
    words = match_expressions("Ana are 50 de mere", [r'[abcd]', r'[1-4]'])
    print(words)

main()