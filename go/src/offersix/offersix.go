package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}


//法一 用栈记录
/*
func reversePrint(head *ListNode) []int {
	res := []int{}
	for head != nil {
		res = append([]int{head.Val}, res...)
		head = head.Next
	}
	return res
}
*/
//法二 第一次记录链表的数量,第二次进行将链表中的值取出并逆序摆放进数组
/*
func reversePrint(head *ListNode) []int {
	cur := head
	n := 0
	for head != nil {
		head = head.Next
		n++
	}
	nums := make([]int, n)
	for {
		if cur == nil {
			break
		}
		nums[n-1] = cur.Val
		cur = cur.Next
		n--
	}
	return nums
}
*/

func reversePrint(head *ListNode) []int {
    var arr []int

	for head != nil {
		arr = append(arr, head.Val)
		head = head.Next
	}

	if len(arr) == 0 {
		return nil
	}

	length := len(arr)
	for i := 0; i < length / 2; i++ {
		temp := arr[i]
		arr[i] = arr[length - i - 1]
		arr[length - i - 1] = temp
	}

	return arr
}


func ListNodePrint(head *ListNode) {
	for head != nil {
		fmt.Println(*head)
		head = head.Next
	}
}

func main() {
	var head = new(ListNode)
	head.Val = 0
	var tail *ListNode
	tail = head
	// 头插法
	/*
	for i := 1; i < 10; i++ {
		var node = ListNode{Val: i}
		node.Next = tail
		tail = &node
	}
	*/
	// 尾插法
	for i := 1; i < 10; i++ {
		var node = ListNode{Val: i}
		(*tail).Next = &node
		tail = &node
	}
	ListNodePrint(head)
	res := reversePrint(head)
	fmt.Println(res)
}