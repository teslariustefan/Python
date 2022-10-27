def main():
    dict_1 = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'e': 4,
            'f': 5,
            'g': 6,
            'h': {
                'i': 7,
                'j': 8,
            }}}

    dict_2 = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': {
            'e': 0,
            'f': 0,
            'g': 0,
            'h': {
                'i': 7,
                'j': 8,
                'k': 9,
                'l': {
                    'm': 10,
                    'n': 11,
                    'o': 12,
                }}}}

    print(compare(dict_1, dict_2))

def compare(dict_1, dict_2):

    if dict_1.keys() != dict_2.keys():
        return False

    for key in dict_1.keys():
        if type(dict_1[key]) == dict:
            if not compare(dict_1[key], dict_2[key]):
                return False

        elif type(dict_1[key]) == tuple or type(dict_1[key]) == set:
            if not compare(dict.fromkeys(dict_1[key]), dict.fromkeys(dict_2[key])):
                return False
                
        else:
            if dict_1[key] != dict_2[key]:
                return False
    return True

main()