#include <iostream>
using namespace std;

typedef struct node{
    int data;
    struct node* next;
    node(int d):data(d), next(NULL){}
}node;

void reverse(node* head){
    if (head == NULL) return;
    node* pleft = NULL;
    node* pcurrent = head;
    node* pright = head->next;

    while(pright){
        pcurrent->next = pleft;
        node *ptemp = pright->next;
        pright->next = pcurrent;
        pleft = pcurrent;
        pcurrent = pright;
        pright = ptemp;
    }

    while(pcurrent != NULL){
        cout<< pcurrent->data << "\t";
        pcurrent = pcurrent->next;
    }
}

