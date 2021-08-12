def firstUniqChar(s):
    if s == "":
        return " "
    dictt = {}
    for i in s:
        if i not in dictt:
            dictt[i] = 1
        else:
            dictt[i] += 1
    for i in s:
        if dictt[i] == 1:
            return i
    return " "
    

s = input()
print(firstUniqChar(s))
