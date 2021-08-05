def shellSort(nums):
    n = len(nums)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            j, num = i-gap, nums[i]
            while j >= 0 and nums[j] > num:
                nums[j+gap] = nums[j]
                j -= gap
            nums[j+gap] = num
        gap = int(gap / 2)
        
nums = [5, 4, 3, 6, 2, 1, 7]
shellSort(nums)
print(nums)
