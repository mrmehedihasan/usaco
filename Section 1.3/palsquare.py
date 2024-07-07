
"""
ID: imehedi2
LANG: PYTHON3
TASK: palsquare 
"""
import string
def base_n(N:int, B:int):
    digits = ""
    digit = "0123456789"+string.ascii_uppercase
    while N:
        digits+=digit[N%B]
        N//=B
    digits = digits[::-1]
    return digits
def is_pal(l):
    r = str(l)[::-1]
    if str(l) == r:
        return True
    else:
        return False
def solve():
    fin = open("palsquare.in", "r")
    fout = open("palsquare.out", "w")
    B = int(fin.readline().strip())
    for i in range(1, 301, 1):
        base = base_n(i**2, B)
        i_base = base_n(i, B)
        if is_pal(base):
            fout.write(f"{i_base} {base}\n")
    fout.close() 
if __name__ == '__main__':
    solve()
