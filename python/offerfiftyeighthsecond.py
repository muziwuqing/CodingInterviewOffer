def reverseChar(s, pstart, pend):
    if pstart == None or pend == None:
        return
    while pstart < pend:
        s[pstart], s[pend] = s[pend], s[pstart]
        pstart += 1
        pend -= 1


def reverseLeftWords(s, n):
    s = list(s)
    length = len(s)
    if length >0 and 0 < n <length:
        reverseChar(s, 0, n-1)
        reverseChar(s, n, len(s)-1)
        reverseChar(s, 0, len(s)-1)
    s = ''.join(s)
    return s


s = ["a", "b", "c", "d", "e", "f"]
n = 2
print(reverseLeftWords(s, n))
