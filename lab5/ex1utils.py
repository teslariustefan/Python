def process_item(arg):
    if arg <= 1:
        return 2
    for i in range(arg + 1, 2 * arg):
        if all(i % j != 0 for j in range(2, i)):
            return i

def main():
    x = int(input("Enter a number: "))
    print(process_item(x))