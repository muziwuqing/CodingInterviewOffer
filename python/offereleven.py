def minArray(numbers):
    left, right = 0, len(numbers) - 1
    while left < right:
        mid = (left + right) >> 1
        if numbers[mid] > numbers[right]:
            left = mid + 1
        elif numbers[mid] < numbers[right]:
            right = mid 
        else:
            right -= 1
    return numbers[left]

numbers = [3, 3, 3, 2, 3]
print(minArray(numbers))
