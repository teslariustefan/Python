import xml.etree.ElementTree as ET

def get_elements(path, attrs):
    tree = ET.parse(path)
    root = tree.getroot()
    elements = []
    for element in root.iter():
        if element.attrib == attrs:
            elements.append(element)
    return elements


def main():
    path = input('Path: ')
    attrs = input('Attrs: ')
    elements = get_elements(path, attrs)
    print(elements)

main()