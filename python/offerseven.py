class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    def helper(preorder, inorder, index, start, end):
        if start > end:
            return None
        root = TreeNode(preorder[index])
        j = start
        while j < end and preorder[index] != inorder[j]:
            j += 1
        root.left = helper(preorder, inorder, index+1, start, j-1)
        root.right = helper(preorder, inorder, index+1+j-start, j+1, end)
        return root
    return helper(preorder, inorder, 0, 0, len(preorder)-1)


def prePrint(root):
    if root == None:
        return
    print(root.val)
    prePrint(root.left)
    prePrint(root.right)


preorder = [1, 2, 4, 8, 5, 3, 6, 7, 9]
inorder = [8, 4, 2, 5, 1, 6, 3, 7, 9]
root = buildTree(preorder, inorder)
prePrint(root)
