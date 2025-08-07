lines = []

def removeblanklines():
    for x in lines:
        if (x == "\n"):
            lines.remove("\n")

def removereturns():
    for x in range(len(lines)):
        lines[x] = lines[x].rstrip()

def removecomments():
    for x in lines:
        if '#' in x:
            lines.remove(x)
            removecomments()

with open("Version1\\Raw.tl", "r") as f:
    lines = f.readlines()
    removeblanklines()
    removereturns()
    print(lines)
    removecomments()
    print(lines)
