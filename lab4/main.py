import os


def ex1(director):
    lista = []
    for nume in os.listdir(director):
        if os.path.splitext(nume)[-1]:
            lista.append(os.path.splitext(nume)[-1])
    lista.sort()
    return set(lista)


def ex2(director, fisier):
    fp = open(fisier, "w")
    for nume in os.listdir(director):
        if nume[0] == "A":
            fp.write(os.path.abspath(nume))
    fp.close()


def ex3(cale):
    if os.path.isfile(cale):
        fp = open(cale, "r")
        return fp.read()[-20:]
    else:
        dictionar = {}
        for nume in os.listdir(cale):
            if dictionar.__contains__(os.path.splitext(nume)[-1]):
                dictionar[os.path.splitext(nume)[-1]] += 1
            else:
                if os.path.splitext(nume)[-1]:
                    dictionar[os.path.splitext(nume)[-1]] = 1
        return dictionar


def ex4(cale):
    lista = []
    for nume in os.listdir(cale):
        if lista.__contains__(os.path.splitext(nume)[-1]):
            pass
        else:
            if (os.path.splitext(nume)[-1] != ""):
                lista.append(os.path.splitext(nume)[-1])
    lista.sort(reverse=True)
    return lista


def ex5(target, to_search):
    lista = []
    if os.path.isfile(target):
        fp = open(target, "r")
        if fp.read().__contains__(to_search):
            lista.append(target)
    elif os.path.isdir(target):
        for nume in os.listdir(target):
            if os.path.isfile(target + '/' + nume):
                fp = open(target + '/' + nume, "r")
                if fp.read().__contains__(to_search):
                    lista.append(nume)
            elif os.path.isdir(nume):
                lista += ex5(nume, to_search)
    else:
        raise ValueError("Nu este un fisier sau director")
    return lista


def callback(nume):
    print(nume + " Nu este un fisier sau director")


def ex6(target, to_search, _callback=None):
    lista = []
    if os.path.isfile(target):
        print('alo')
        fp = open(target, "r")
        if fp.read().__contains__(to_search):
            lista.append(target)
    elif os.path.isdir(target):
        for nume in os.listdir(target):
            if os.path.isfile(target + '/' + nume):
                fp = open(target + '/' + nume, "r")
                if fp.read().__contains__(to_search):
                    lista.append(nume)
            elif os.path.isdir(nume):
                lista += ex5(nume, to_search)
    else:
        callback(target)
    return lista


def ex7(cale):
    dictionar = {}
    dictionar['full_path'] = os.path.abspath(cale)
    dictionar['file_size'] = os.path.getsize(cale)
    dictionar['file_extension'] = os.path.splitext(cale)[-1]
    dictionar['can_read'] = os.access(cale, os.R_OK)
    dictionar['can_write'] = os.access(cale, os.W_OK)
    return dictionar


def ex8(dir_path):
    lista = []
    for nume in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, nume)):
            lista.append(os.path.abspath(nume))
    return lista


if __name__ == '__main__':
    print("Exercitiu 1 pentru directortest:")
    print(ex1("directortest"))
    print("Exercitiu2 pentru directortest in fisiernou")
    ex2("directortest", "fisier_nou")
    print("Exercitiu 3:")
    print(ex3("directortest"))
    print('Exercitiu 4:')
    print(ex4("directortest"))
    print('Exercitiu 5:')
    print(ex5('directortest', 'cuvant'))
    print('Exercitiu 6:')
    print(ex6('directorNuExista', 'cuvant', callback))
    print('Exercitiu 7:')
    print(ex7('directortest'))
    print('Exercitiu 8:')
    print(ex8('directortest'))
