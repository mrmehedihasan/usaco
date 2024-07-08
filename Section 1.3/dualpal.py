"""
ID: imehedi2
LANG: PYTHON3
TASK: dualpal
"""
import string
def base_n(N:int, B:int):
    digits = ""
    digit = "0123456789"+string.ascii_uppercase
    while N:
        digits+=digit[N%B]
        N//=B
    digits = digits[::-1]
    return int(digits)

def is_pal(l):
    r = str(l)[::-1]
    if int(str(l)) == int(r):
        return True
    else:
        return False

def solve():
    fin = open("dualpal.in", "r")
    fout = open("dualpal.out", "w")
    f,s = fin.readline().strip().split(" ")
    f=int(f)
    s=int(s)
    s+=1
    while f>0:
        cnt = 0        
        for i in range(2, 11, 1):
            if(is_pal(base_n(s, i))):
                cnt+=1
            if cnt>=2:
                fout.write(str(s)+'\n')
                f-=1
                cnt = 0
                break
        s+=1

if __name__ == "__main__":
    solve()