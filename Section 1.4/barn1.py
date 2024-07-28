"""
ID: imehedi2
LANG: PYTHON3
TASK: barn1
"""

def solve():
    fin = open("barn1.in", "r")
    fout = open("barn1.out", "w")
    sheet, stalls, cow = fin.readline().strip().split(" ")
    sheet, stalls, cow = int(sheet), int(stalls), int(cow)
    cows = []
    for _ in range(cow):
        c = int(fin.readline().strip())
        cows.append(c)

    cows.sort()
    stalls = cows[len(cows)-1] - cows[0]

    empty_stalls = []

    f = cows[0]
    for i in range(1, cow):
        d = cows[i] - f
        if d > 1:
            empty_stalls.append(d-1)
        f = cows[i]

    empty_stalls.sort(reverse=True)
    out = 0
    if sheet>=len(cows):
        sheet = len(cows)
    for i in range(0, sheet-1):
        out+=empty_stalls[i]
        print(empty_stalls[i])

    
    fout.write(f"{stalls-out+1}\n")

    
if __name__ == "__main__":
    solve()