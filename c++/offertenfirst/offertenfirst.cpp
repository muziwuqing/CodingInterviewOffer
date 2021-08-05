#include <iostream>
using namespace std;

int fib(int n){
    int a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        int tmp = (a + b) % 1000000007;
        a = b;
        b = tmp;
    }
    return a;
}


int main(){
    cout<<fib(47)<<endl;
    system("pause");
    return 0;
}