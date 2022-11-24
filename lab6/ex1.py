def extract_words(inputtxt):
    words = []
    word = ''
    for i in inputtxt:
        if i.isalnum():
            word += i
        else:
            if word != '':
                words.append(word)
            word = ''
    if word != '':
        words.append(word)    
    return words


def main():
    inputtxt = input('Enter text: ')
    words = extract_words(inputtxt)
    print(words)


if __name__ == '__main__':
    main()