def findTarget(nums, target):
    temp=nums.copy()
    temp.sort()
    i=0
    j=len(nums)-1
    while i<j:
        if (temp[i]+temp[j])>target:
            j=j-1
        elif (temp[i]+temp[j])<target:
            i=i+1
        else:
            break
    p=nums.index(temp[i])
    nums.pop(p)
    k=nums.index(temp[j])
    if k == p:
        k=k+1
    if p > k:
        p, k = k, p
    return [p,k]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    res = findTarget(nums, target)
    print(res)
