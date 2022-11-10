def makecalculus(pairs):
    return list(map(lambda x: {'sum': x[0] + x[1], 'prod': x[0] * x[1], 'pow': x[0] ** x[1]}, pairs))

def main():
    print(makecalculus([(2, 1), (9, 1), (30, 6), (2, 2)]))

main()