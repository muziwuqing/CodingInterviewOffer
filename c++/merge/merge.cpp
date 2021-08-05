#include <iostream>
using namespace std;

int tmp[10010] = {};

void mergeSort(int nums[], int left, int right) {
    if (left >= right) {
        return;
    }
    int mid = (left + right) >> 1;
    mergeSort(nums, left, mid);
    mergeSort(nums, mid + 1, right);
    int i = left, j = mid + 1, k = 0;
    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j]) {
            tmp[k++] = nums[i++];
        } else {
            tmp[k++] = nums[j++];
        }
    }
    while (i <= mid) {
        tmp[k++] = nums[i++];
    }
    while (j <= right) {
        tmp[k++] = nums[j++];
    }
    for (i = left, j = 0; i <= right; ++i, ++j) {
        nums[i] = tmp[j];
    }
}

int main() {
    int n;
    cin>>n;
    int nums[n] = {};
    for (int i = 0; i < n; ++i) {
        cin>>nums[i];
    }
    mergeSort(nums, 0, n - 1);
    for (int i = 0; i < n; ++i) {
        printf("%d ", nums[i]);
    }
    system("pause");
    return 0;
}