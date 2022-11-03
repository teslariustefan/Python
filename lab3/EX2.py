
def main():
    print(ct_letters("Lab 3 python"))

def ct_letters(text):
    result = {}
    for letter in text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

main()