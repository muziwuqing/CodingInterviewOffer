package main

import "fmt"

type TreeNode struct {
	Val int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 {
        return nil
    }
    root := &TreeNode{preorder[0], nil, nil}
    stack := []*TreeNode{}
    stack = append(stack, root)
    var inorderIndex int
    for i := 1; i < len(preorder); i++ {
        preorderVal := preorder[i]
        node := stack[len(stack)-1]
        if node.Val != inorder[inorderIndex] {
            node.Left = &TreeNode{preorderVal, nil, nil}
            stack = append(stack, node.Left)
        } else {
            for len(stack) != 0 && stack[len(stack)-1].Val == inorder[inorderIndex] {
                node = stack[len(stack)-1]
                stack = stack[:len(stack)-1]
                inorderIndex++
            }
            node.Right = &TreeNode{preorderVal, nil, nil}
            stack = append(stack, node.Right)
        }
    }
    return root
}



//方法一  按正常思路来
/*
func buildTree(preorder []int, inorder []int) *TreeNode {
	return helper(preorder, inorder, 0, 0, len(preorder)-1)
}

func helper(preorder, inorder []int, index, start, end int) *TreeNode {
	if start > end {
		return nil
	}
	root := &TreeNode{Val: preorder[index]}
	j := start
	for j < end && preorder[index] != inorder[j] {
		j++
	}
	root.Left = helper(preorder, inorder, index+1, start, j-1)
	root.Right = helper(preorder, inorder, index+1+j-start, j+1, end)
	return root
}
*/
func prePrint(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	prePrint(root.Left)
	prePrint(root.Right)
}

func main() {
	preorder := []int{1, 2, 4, 8, 5, 3, 6, 7, 9}
	inorder := []int{8, 4, 2, 5, 1, 6, 3, 7, 9}
	root := buildTree(preorder, inorder)
	prePrint(root)
}