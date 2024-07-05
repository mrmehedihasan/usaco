"""
ID: imehedi2
LANG: PYTHON3
TASK: namenum
"""
def read_file():
    lines = []
    with open("dict.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

MAP = {
    "2" : ["A", "B", "C"],
    "3" : ["D", "E", "F"],
    "4" : ["G", "H", "I"],
    "5" : ["J", "K", "L"],
    "6" : ["M", "N", "O"],
    "7" : ["P", "R", "S"],
    "8" : ["T", "U", "V"],
    "9" : ["W", "X", "Y"]
}


#ABCD
def solve():
    fin = open("namenum.in", "r")
    fout = open("namenum.out", "w")
    inp = str(fin.readline().strip())
    words = read_file()
    i = 0
    _word = []

    for word in words:
        if(len(word) == len(inp)):
            _word.append(word)
    words = _word
    i = 0
    for char in inp:
        words_ = []
        for word in words:
            if word[i] == MAP[char][0] or word[i] == MAP[char][1] or word[i] == MAP[char][2]:
               words_.append(word)
        words = words_
        if(len(words) == 0):
            break
        i+=1
    if(len(words) == 0):
        fout.write(str("NONE\n"))
    else:
        for word in words:
            fout.write(str(word) + '\n')
    fout.close()
solve()
