import heapq

def getLeastNumbers(arrs, k):
    heap = []
    for arr in arrs:
        if len(heap) <= k:
            heapq.heappush(heap, -arr)
        else:
            if heapq.nsmallest(1, heap) < -arr:
                heapq.heapreplace(heap, -arr)
    res = [-i for i in heap]
    return res


if __name__ == '__main__':
    arrs = list(map(int, input().split()))
    k = int(input())
    res = getLeastNumbers(arrs, k)
    print(res)
