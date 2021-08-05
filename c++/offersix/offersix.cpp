#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

/* 栈实现
vector<int> reversePrint(ListNode* head){
    stack<int> Stack;
    ListNode* p = head;
    while (p != NULL) {
        Stack.push(p->val);
        p = p->next;
    }
    vector<int> res;
    while (!Stack.empty()){
        int tmp = Stack.top();
        Stack.pop();
        res.push_back(tmp);        
    }
    return res;
}
*/

vector<int> reversePrint(ListNode* head){
    ListNode* p = head;
    int count = 0;
    while (p != NULL) {
        p = p->next;
        count++;
    }
    vector<int> res(count);
    while (head != NULL) {
        res[--count] = head->val;
        head = head->next;
    }
    return res;
}


int main(){
    ListNode* head = new ListNode(0);
    ListNode* tail = head;
    for (int i=1; i<10; i++) {
        ListNode* node = new ListNode(i);
        tail->next = node;
        tail = tail->next;
    }
    vector<int> res = reversePrint(head);
    for (int i=0; i<res.size(); i++) {
        cout<<res[i]<<" ";
    }
    cout<<endl;
    system("pause");
    return 0;
}