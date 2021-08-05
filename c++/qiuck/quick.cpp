#include <iostream>
using namespace std;

void quickSort(int nums[], int left, int right){
    if (left >= right) return;
    int i = left - 1;
    int j = right + 1;
    int x = nums[left];
    while (i < j) {
        while (nums[++i] < x);
        while (nums[--j] > x);
        if (i < j) {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
    quickSort(nums, left, j);
    quickSort(nums, j+1, right);
}

int main(){
    int nums[] = {4, 3, 5, 2, 7, 6};
    quickSort(nums, 0, 5);
    for (int i=0; i<6; i++){
        cout<<nums[i]<<" ";
    }
    cout<<endl;
    system("pause");
    return 0;
}