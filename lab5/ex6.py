def pairs_get(my_list):
    zero = list(filter(lambda x: x % 2 == 0, my_list))
    one = list(filter(lambda x: x % 2 != 0, my_list))
    return list(zip(zero, one))

def main():
    print(pairs_get([0, 4, 4, 5, 8, 2, 4, 10, 9, 2]))

main()