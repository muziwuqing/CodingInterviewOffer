#include <iostream>
using namespace std;

void change(int nums[], int i, int j){
    int tmp = nums[i];
    nums[i] = nums[j];
    nums[j] = tmp;
}

void selectSort(int nums[], int size){
    for (int i=0; i < size-1; i++){
        int minIndex = i;
        for (int j=i+1; j < size; j++){
            if (nums[j] < nums[minIndex]){
                minIndex = j;
            }
        }
        change(nums, i, minIndex);
    }
}

void printArray(int nums[], int size){
    for (int i=0; i < size; i++){
        cout<<nums[i]<<" ";
    }
}

int main(){
    int nums[] = {2, 1, 6, 4, 7, 9, 5};
    int size = 7;
    selectSort(nums, size);
    printArray(nums, size);
    cout<<endl;
    system("pause");
    return 0;
}