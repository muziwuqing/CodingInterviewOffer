#include <iostream>
#include <stack>
using namespace std;

class CQueue {
private:
    stack<int> in;
    stack<int> out;
public:
    CQueue() {

    }
    
    void appendTail(int value) {
        in.push(value);
    }
    
    int deleteHead() {
        while (!out.empty()){
            int res = out.top();
            out.pop();
            return res;
        }
        while (!in.empty()){
            int tmp = in.top();
            in.pop();
            out.push(tmp);
        }
        if (out.empty()){
            return -1;
        }
        int tmp = out.top();
        out.pop();
        return tmp;

    }
};



int main(){
    CQueue* obj = new CQueue();
    obj->appendTail(2);
    obj->appendTail(3);
    int param_1 = obj->deleteHead();
    cout<<param_1<<endl;
    system("pause");
    return 0;
}