def missingNumber(nums):
    if len(nums) == 0:
        return -1
    length = len(nums)
    l, r = 0, length - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] != mid:
            if mid == 0 or nums[mid - 1] == mid - 1:
                return mid
            r = mid - 1
        else:
            l = mid + 1
    if l == length:
        return length

nums = [0, 1, 2, 3, 4, 6]
print(missingNumber(nums))
