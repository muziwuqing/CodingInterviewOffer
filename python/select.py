def selectionSort(nums):
    for i in range(len(nums) - 1):
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[minIndex], nums[i] = nums[i], nums[minIndex]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    selectionSort(nums)
    print(nums)