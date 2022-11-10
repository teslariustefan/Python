def num_get(my_list):
    return list(filter(lambda x: type(x) == int or type(x)==float, my_list))

def main():
    print(num_get([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

main()