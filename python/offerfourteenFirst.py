def cuttingRope(n):
    if n < 4:
        return n - 1
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    return res * n


n = int(input())
res = cuttingRope(n)
print(res)
