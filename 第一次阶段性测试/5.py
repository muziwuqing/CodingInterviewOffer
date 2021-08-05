def findMax(nums):
    res = []
    maxnum = -999999
    for i in range(len(nums)):
        if len(res) == 0:
            maxnum = nums[i]
            res.append(i)
        if nums[i] > maxnum:
            res.clear()
            maxnum = nums[i]
            res.append(i)
        elif nums[i] == maxnum:
            res.append(i)
    return res


nums = list(map(int, input().split()))
print(findMax(nums))
