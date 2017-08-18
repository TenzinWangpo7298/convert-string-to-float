#python3 tenzin
def changenum(data):
    foo = ""
    for i in list(data):
        if i == ",":
            continue
        else:
            foo += i
    return  float(int(foo))