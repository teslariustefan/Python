
def main():
    print(xml("a", "hello world!", href="http://python.org", _class="my-link", id="someid"))

def xml(tag, content, **kwargs):
    result = "<" + tag
    for key, value in kwargs.items():
        result += " " + key + "=\"" + value + "\""
    result += ">" + content + "</" + tag + ">"
    return result
    
main()