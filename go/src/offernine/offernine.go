package main

import "fmt"

type CQueue struct {
	Stack1 []int
	Stack2 []int
}

func Constructor() CQueue {
	return CQueue{Stack1: []int{}, Stack2: []int{}}
}

func (this *CQueue) AppendTail(value int) {
	this.Stack1 = append(this.Stack1, value)
}

func (this *CQueue) DeleteHead() int {
	if len(this.Stack1) == 0 && len(this.Stack2) == 0 {
		return -1
	}
	if len(this.Stack2) > 0 {
		res := this.Stack2[len(this.Stack2)-1]
		this.Stack2 = this.Stack2[0 : len(this.Stack2)-1]
		return res
	}
	for len(this.Stack1) > 0 {
		this.Stack2 = append(this.Stack2, this.Stack1[len(this.Stack1)-1])
		this.Stack1 = this.Stack1[0 : len(this.Stack1)-1]
	}
	res := this.Stack2[len(this.Stack2)-1]
	this.Stack2 = this.Stack2[0 : len(this.Stack2)-1]
	return res
}

func main() {
	obj := Constructor()
	obj.AppendTail(2)
	obj.AppendTail(3)
	param_1 := obj.DeleteHead()
	fmt.Println(param_1)
}