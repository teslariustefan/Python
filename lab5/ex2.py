def argsum(*args, **kwargs):
    return sum(kwargs.values())

argsum2 = lambda *args,**kwargs: sum(kwargs.values()) 


def main():
    print(argsum(1, 2, c=4, d=5))
    print(argsum2(1, b=3, c=4, d=5))

main()