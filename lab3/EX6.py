
def main():
    print(ct_unique_duplicate([0, 8, 3, 9, 5, 1, 2, 3, 4, 5, 6, 7, 8, 10, 10]))

def ct_unique_duplicate(lst):
    unique = set(lst)
    return len(unique), len(lst) - len(unique)

main()