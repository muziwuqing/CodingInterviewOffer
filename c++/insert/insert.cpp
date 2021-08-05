#include <iostream>
using namespace std;

void insertSort(int nums[], int size){
    for (int i=1; i<size; i++){
        int j = i-1;
        int num = nums[i];
        for (; j>=0 && nums[j]>num;j--){
            nums[j+1] = nums[j];
        }
        nums[j+1] = num;

    }
}

void printArray(int nums[], int size){
    for (int i=0; i<size; i++){
        cout<<nums[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int nums[] = {3, 2, 5, 1, 6, 4};
    int size = 6;
    insertSort(nums, size);
    printArray(nums, size);
    system("pause");
    return 0;
}