#include <iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int * nums = new int [n];
    nums[0] = 1;
    nums[1] = 2;
    for (int i=0; i<n; i++) {
        cout<<nums[i]<<" ";
    }
    cout<<endl;
    system("pause");
    return 0;
}