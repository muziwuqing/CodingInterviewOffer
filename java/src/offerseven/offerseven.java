package offerseven;

public class offerseven{
    public static class TreeNode{
        int value;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) {value = x;}
    }
    public static TreeNode bulidTree(int []preorder, int []inorder){
        return helper(preorder, inorder, 0, 0, preorder.length-1);
    }

    public static TreeNode helper(int []preorder, int []inorder, int index, int start, int end){
        if (start > end) return null;
        int j = 0;
        while (j < preorder.length && preorder[index] != inorder[j]) {
            j++;
        }
        TreeNode root = new TreeNode(preorder[index]);
        root.left = helper(preorder, inorder, index+1, start, j-1);
        root.right = helper(preorder, inorder, index+1+j-start, j+1, end);
        return root;
    }

    public static void prePrint(TreeNode root){
        if (root == null) return;
        System.out.println(root.value);
        prePrint(root.left);
        prePrint(root.right);
    }

    public static void main(String[] args) {
        int []preorder = new int[]{1, 2, 4, 8, 5, 3, 6, 7, 9};
        int []inorder = new int[]{8, 4, 2, 5, 1, 6, 3, 7, 9};
        TreeNode root = bulidTree(preorder, inorder);
        prePrint(root);
    }
}