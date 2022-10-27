
def main():
    print(list({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

def list(map):
    result = []
    key = map["start"]
    while key not in result:
        result.append(key)
        key = map[key]
    return result

main()