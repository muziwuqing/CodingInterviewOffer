# 三数之和，三指针，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组
def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()
    res = []
    for k in range(len(nums)):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue
        l, r = k + 1, len(nums) - 1
        while l < r:
            if (nums[k] + nums[l] + nums[r] == 0):
                res.append([nums[k], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l = l + 1
                while l < r and nums[r] == nums[r-1]:
                    r = r - 1
                l = l + 1
                r = r - 1
            elif nums[k] + nums[l] + nums[r] > 0:
                r = r - 1
            else:
                l = l + 1
    return res


nums = [0, 0, 0]
print(threeSum(nums))
