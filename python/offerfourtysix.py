# f(i) = f(i+1) + g(i, i+1) * f(i+2) <10 ~ 25>
def translateNum(nums):
    if nums<0:
        return 0
    nums = list(map(int, list(str(nums))))
    length = len(nums)
    dp = [0] * length
    for i in range(length-1, -1, -1):
        if i < length-1:
            dp[i] = dp[i+1]
        else:
            dp[i] = 1
        if i < length - 1:
            if 10 <= nums[i] * 10 + nums[i+1] <= 25:
                if i < length - 2:
                    dp[i] += dp[i+2]
                else:
                    dp[i] += 1
    return dp[0]



nums = int(input())
print(translateNum(nums))
