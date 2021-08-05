#include <iostream>
#include <vector>
using namespace std;

int minArray(vector<int> numbers){
    int l = 0, r = numbers.size()-1;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (numbers[mid] > numbers[r]) {
            l = mid+1;
        } else if (numbers[mid] < numbers[l]) {
            r = mid;
        } else {
            r--;
        }
    }
    return numbers[l];
} 

int main(){
    vector<int> numbers = {4, 5, 1, 2, 3};
    cout<<minArray(numbers)<<endl;
    system("pause");
    return 0;
}