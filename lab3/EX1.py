def main():
    print(sets([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

def sets(a, b):
    return [set(a).intersection(b), set(a).union(b), set(a).difference(b), set(b).difference(a)]

main()