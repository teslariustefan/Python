def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    S = 'This is a test string'
    print([i for i in S 
        if i in vowels])
    print(list(filter(lambda i: i in vowels, S)))
    print(list(filter(lambda i: i in vowels, list(S))))

main()