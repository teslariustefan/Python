
def main():
    print(ct_args(5, 2, 0, 4, x=5, y=2, z=0, w=9))

def ct_args(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count

main()