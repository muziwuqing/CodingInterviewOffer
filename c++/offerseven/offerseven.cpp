#include <iostream>
#include <vector>
using namespace std;

struct TreeNode{
    int value;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : value(x){}
};

TreeNode* helper(vector<int> preorder, vector<int> inorder, int index, int start, int end){
    if (start>end) return NULL;
    int j = 0;
    while (j<preorder.size() && preorder[index] != inorder[j]){j++;}
    TreeNode* root = new TreeNode(preorder[index]);
    root->left = helper(preorder, inorder, index+1, start, j-1);
    root->right = helper(preorder, inorder, index+1+j-start, j+1, end);
    return root;
}

TreeNode* buildTree(vector<int> preorder, vector<int> inorder){
    return helper(preorder, inorder, 0, 0, preorder.size()-1);
}

void prePrint(TreeNode* root){
    if (root == NULL) return;
    cout<<root->value<<endl;
    prePrint(root->left);
    prePrint(root->right);
}

int main(){
    vector<int> preorder = {1, 2, 4, 8, 5, 3, 6, 7, 9};
    vector<int> inorder = {8, 4, 2, 5, 1, 6, 3, 7, 9};
    TreeNode* root = buildTree(preorder, inorder);
    prePrint(root);
    system("pause");
    return 0;
}