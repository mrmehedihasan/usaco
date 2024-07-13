
"""
ID: imehedi2
LANG: PYTHON3
TASK: milk
"""


MAX = 1001

amnt_for_price = [0]*MAX

def solve():
    fin = open("milk.in", "r")
    fout = open("milk.out", "w")

    milkReq, numFar = fin.readline().strip().split() # type: ignore
    milkReq, numFar = int(milkReq), int(numFar)

    for _ in range(numFar):
        p, q = fin.readline().strip().split()
        p, q = int(p), int(q)
        amnt_for_price[p]+=q

    price_total = 0
    milk_total = 0
    for i in range(MAX):
        if(amnt_for_price[i]!=0):
            if (milk_total+amnt_for_price[i]) < milkReq:
                price_total += (amnt_for_price[i]*i)
                milk_total += amnt_for_price[i]
            else:
                need = milkReq-milk_total
                price_total += (need*i)
                break
    fout.write(str(price_total) + "\n")

if __name__ == '__main__':
    solve()