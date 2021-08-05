def findMax(nums):
    maxnum = max(nums)
    count = nums.count(maxnum)
    res = []
    while count > 0:
        index = nums.index(maxnum)
        res.append(index)
        nums[index] = -9999
        count -= 1
    return res

nums = list(map(int, input().split()))
print(findMax(nums))
