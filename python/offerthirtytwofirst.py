class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Creat_Tree(root,val):
    if len(val)==0:#终止条件：val用完了
        return root
    if val[0]!='#':#本层需要干的就是构建root、root.lchild、root.rchild三个节点。
        root = TreeNode(val[0])
        val.pop(0)
        root.left = Creat_Tree(root.left,val)
        root.right = Creat_Tree(root.right,val)
        return root#本次递归要返回给上一次的本层构造好的树的根节点
    else:
        root=None
        val.pop(0)
        return root#本次递归要返回给上一次的本层构造好的树的根节点

def levelOrder(root):
    if root == None:
        return
    queue = []
    path = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        path.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return path    
    



root = None
arrs = "abc##d##e##"
val = list(arrs)
Creat_Tree(root, val)
print(levelOrder(root))

