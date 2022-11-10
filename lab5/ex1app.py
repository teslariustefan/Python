from ex1utils import process_item

def main():
    while True:
        i = input("Enter a number: ")
        if i == "q":
            break
        print(process_item(int(i)))

main()