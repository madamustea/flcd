reservedWords = []
separators = []
operators = []


def readFile():
    with open('Token.in', 'r') as f:
        f.readline()
        for i in range(20):
            reservedWords.append(f.readline().strip())
        for i in range(21):
            operators.append(f.readline().strip())
        for i in range(9):
            separator = f.readline().strip()
            if separator == "<space>":
                separator = " "
            separators.append(separator)

