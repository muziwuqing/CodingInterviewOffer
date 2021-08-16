from itertools import chain

def maxSubArray(nums):
    if len(nums) == 0:
        return 0
    dp = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        if i == 0 or dp[i-1] <= 0:
            dp[i] = nums[i]
        elif i != 0 and dp[i-1] > 0:
            dp[i] = dp[i-1] + nums[i]
    return max(dp)


nums = [2, 3, 4, 2, 1, 5, 6]
print(maxSubArray(nums))
