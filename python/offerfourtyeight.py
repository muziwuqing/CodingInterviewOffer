def lengthOfLongestSubstring(s):
    dic = {}
    res = tmp = 0
    for j in range(len(s)):
        i = dic.get(s[j], -1)
        dic[s[j]] = j
        tmp = tmp + 1 if tmp < j - i else j - i
        res = max(res, tmp)
    return res


s = input()
print(lengthOfLongestSubstring(s))
