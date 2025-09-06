lines = []


def removeblanklines():
    for x in lines:
        if (x == "\n"):
            lines.remove("\n")
            removeblanklines()

def removereturns():
    for x in range(len(lines)):
        lines[x] = lines[x].rstrip()

def removecomments():
    for x in lines:
        if '#' in x:
            lines.remove(x)
            removecomments()

with open("Version2\\Raw.tl", "r") as f:
    lines = f.readlines()
    removeblanklines()
    removereturns()
    print(lines)
    removecomments()
    print(lines)
    with open("Version2\\processed.tl", "w") as p:
        output = ""
        for x in lines:
            output += x + "\n"
        p.write(output)
