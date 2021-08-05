romaDict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def romanToInt(s):
    ans = 0
    n = len(s)
    for i, ch in enumerate(s):
        value = romaDict[ch]
        if i < n - 1 and value < romaDict[s[i + 1]]:
            ans -= value
        else:
            ans += value
    return ans

s = input()
print(romanToInt(s))
