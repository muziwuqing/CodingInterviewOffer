def quickSort(nums, left, right):
    if left >= right:
        return
    i, j = left-1, right+1
    x = nums[left]
    while i < j:
        while True:
            i += 1
            if nums[i] >= x:
                break
        while True:
            j -= 1
            if nums[j] <= x:
                break
        if i < j :
            nums[i], nums[j] = nums[j], nums[i]
    quickSort(nums, left, j)
    quickSort(nums, j+1, right)


if __name__ == '__main__':
    nums = [4, 3, 5 ,2, 6]
    quickSort(nums, 0, len(nums)-1)
    print(nums)