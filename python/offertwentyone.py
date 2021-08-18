def exchange(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        while nums[r] % 2 == 0 and l < r:
            r -= 1
        while nums[l] % 2 == 1 and l < r:
            l += 1
        nums[r], nums[l] = nums[l], nums[r]
    return nums



nums = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
print(exchange(nums))
