
def main():
    print(sets({3,4}, {1, 2}))

def sets(*sets):
    result = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            result[f"{a} | {b}"] = a.union(b)
            result[f"{a} & {b}"] = a.intersection(b)
            result[f"{a} - {b}"] = a.difference(b)
            result[f"{b} - {a}"] = b.difference(a)
    return result

main()