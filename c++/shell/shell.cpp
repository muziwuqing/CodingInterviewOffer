#include <iostream>
using namespace std;


void shellSort(int nums[], int size){
    int gap = size / 2;
    for (; gap>0; gap/=2){
        for(int i=gap; i<size; i++){
            int j = i - gap;
            int num = nums[i];
            for (; j>=0 && nums[j]>num; j-=gap){
                nums[j+gap] = nums[j];
            }
            nums[j+gap] = num;
        }
    }
}


int main(){
    int nums[] = {4, 3, 6, 5, 1, 7, 2, 8, 9};
    int size = 9;
    shellSort(nums, size);
    for (int i=0; i<size; i++){
        cout<<nums[i]<<" ";
    }
    cout<<endl;
    system("pause");
    return 0;
}