def maxArea(height):
    res = [[0 for _ in range(len(height))] for _ in range(len(height))]
    result = 0
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            res[i][j] = (j - i) * min(height[i], height[j])
            if res[i][j] > result:
                result = res[i][j]
    return result


def maxArea(height):
    pass

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
