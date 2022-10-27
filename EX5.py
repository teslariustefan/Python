
def main():
    s={("key1", "", "here", ""), ("key2", "start", "middle", "winter")}
    d= {"key1": "come here, it's too cold out", "key3": "this is not valid"}
    print(validate(s,d))

def validate(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]
        if not value.startswith(prefix) or not value.endswith(suffix) or middle not in value[1:-1]:
            return False
    return True

main()