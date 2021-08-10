#include <iostream>
#include <vector>
using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x){val=x;}
};

ListNode* reverseList(ListNode *head){
    // ListNode *rhead = new ListNode(0);
    // rhead->next = NULL;
    // while (head != NULL) {
    //     ListNode *node = new ListNode(head->val);
    //     node->next = rhead->next;
    //     rhead->next = node;
    //     head = head->next;
    // }
    // return rhead;
    ListNode *pre = NULL, *cur = head;
    while (cur) {
        ListNode* temp = cur->next;
        cur->next = pre;
        pre = cur;
        cur = temp;
    }
    return pre;
}

void printList(ListNode *head) {
    while (head != NULL) {
        cout<<head->val<<" ";
        head = head->next;
    }
}

ListNode* constructList(vector<int> arr) {
    ListNode *head = NULL;
    ListNode *tail = head;
    for (int i=0; i<arr.size(); i++) {
        ListNode *node = new ListNode(arr[i]);
        tail->next = node;
        tail = tail->next;
    }
    return head;
}

int main(){
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    ListNode *head = constructList(arr);
    printList(head);
    ListNode *res = reverseList(head);
    printList(res);
    system("pause");
    return 0;
}