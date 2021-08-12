def search(nums, target):
    if len(nums) == 0:
        return 0
    l, r = 0, len(nums) - 1
    left, right = -1, -1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            if mid == 0 or mid > 0 and nums[mid - 1] != target:
                left = mid
                break
            else:
                r = mid - 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    if left == -1 :
        return 0
    l, r = 0, len(nums)
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            if mid == len(nums) - 1 or mid < len(nums) and nums[mid + 1] != target:
                right = mid
                break
            else:
                l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return right - left + 1

nums = [1]
target = 1
print(search(nums, target))
