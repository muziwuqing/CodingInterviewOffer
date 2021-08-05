#include <iostream>
using namespace std;


void swap(int nums[], int i, int j){
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void bubbleSort(int nums[], int size){
    bool hasChanged = true;
    for (int i = 0, n = size; i < n - 1 && hasChanged; i++){
        hasChanged = false;
        for (int j = 0; j < n-i-1; j++){
            if (nums[j] > nums[j+1]){
                swap(nums, j, j+1);
                hasChanged = true;
            }
        }
    }
}

void printArray(int nums[], int size){
    int n = size;
    for (int i = 0; i < n; i++){
        cout<<nums[i]<<" ";
    }
}

int main(){
    int nums[] = {2, 1, 6, 4, 7, 9, 5};
    int size = 7;
    bubbleSort(nums, size);
    printArray(nums, size);
    cout<<endl;
    system("pause");
    return 0;
}