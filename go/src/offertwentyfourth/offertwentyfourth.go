package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil{
		return head
	}
	rhead := &ListNode{}
	head = head.Next
	cur := head
	for cur != nil {
		tmp := cur.Next
		cur.Next = rhead.Next
		rhead.Next = cur
		cur = tmp
	}
	return rhead
}

func printList(head *ListNode) {
	head = head.Next
	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}
}

func constructList(arr []int) *ListNode {
	head := &ListNode{}
	p := head
	for i := 0; i < len(arr); i++ {
		node := &ListNode{Val:arr[i]}
		p.Next = node
		p = p.Next
	}
	return head
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7}
	ln := constructList(arr)
	printList(ln)
	res := reverseList(ln)
	printList(res)
}