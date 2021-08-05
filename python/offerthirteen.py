def movingCount(m, n, k):
    isVisited = [[0 for _ in range(n)] for _ in range(m)]
    res = dfs(m, n, k, isVisited, 0, 0)
    return res


def dfs(m, n, k, isVisited, i, j):
    res = 0
    if check(m, n, k, isVisited, i, j):
        isVisited[i][j] = 1
        res = 1  + dfs(m, n, k, isVisited, i+1, j) + dfs(m, n, k, isVisited, i, j+1)
    return res


def check(m, n, k, isVisited, i, j):
    if 0 <= i < m and 0 <= j < n and getDigitSum(i) + getDigitSum(j) <= k and isVisited[i][j] == 0:
        return True
    return False


def getDigitSum(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number = number // 10
    return summ


m, n, k = list(map(int, input().split()))
res = movingCount(m, n, k)
print(res)
