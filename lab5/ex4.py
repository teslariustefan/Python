def dicts(*args, **kwargs):
    a = list(filter(lambda x: type(x) == dict and len(x) >= 2 and any(type(y) == str and len(y) >= 3 for y in x.keys()), args))
    b = list(filter(lambda x: type(x) == dict and len(x) >= 2 and any(type(y) == str and len(y) >= 3 for y in x.keys()), kwargs.values()))

    return a + b

def main():
    print(dicts( {1: 2, 3: 4, 5: 6},  {'a': 5, 'b': 7, 'c': 'e'}, {2: 3}, [1, 2, 3], {'abc': 4, 'def': 5}, 3764,
                     dict={'ab': 4, 'ac': 'abcde', 'fg': 'abc'}, testdata={1: 1, 'test': True}))

main()