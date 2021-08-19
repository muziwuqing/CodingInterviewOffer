def myPow(x, n):
    isInvalid = False
    if x == 0.0 and n < 0:
        isInvalid = True
        return 0.0
    absn = n
    if n < 0:
        absn = -n
    result = pwue(x, absn)
    if n < 0:
        result = 1.0 / result
    return result

def pwue(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    result = pwue(x, n>>1)
    result *= result
    if n & 0x1 == 1:
        result *= n
    return result

print(myPow(2.00000, 10))
