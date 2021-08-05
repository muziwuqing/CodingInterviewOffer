def insertSort(nums):
    for i in range(1, len(nums)):
        j, num = i-1, nums[i]
        while j >= 0 and nums[j] > num:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = num


if __name__ == '__main__':
    nums = [4, 3, 5, 1, 7, 2]
    insertSort(nums)
    print(nums)
