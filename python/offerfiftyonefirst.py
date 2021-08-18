def reverseWords(s):
    sl = list(s.split(" "))
    rest = []
    for i in range(len(sl)):
        if sl[i] != "":
            rest.append(reverse(sl[i]))
    res = " ".join(rest)
    res = reverse(res)
    return res

def reverse(st):
    st = list(st)
    l, r = 0, len(st) - 1
    while l < r:
        st[l], st[r] = st[r], st[l]
        l += 1
        r -= 1
    return "".join(st)

s = "  hello world!  "
print(reverseWords(s))


