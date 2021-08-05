package main

import "fmt"

func quickSort(nums []int, left, high int){
	if left >= high {
		return 
	}
	i, j := left-1, high+1
	x := nums[(left+high)>>1]
	for i < j {
		for {
			i++
			if nums[i] >= x {
				break
			}
		}
		for {
			j--
			if nums[j] <= x{
				break
			}
		}
		if i < j {
			nums[i], nums[j] = nums[j], nums[i]
		}
	}
	quickSort(nums, left, j)
	quickSort(nums, j+1, high)
}

func main(){
	nums := []int{2, 5, 6, 4, 1, 7}
	quickSort(nums, 0, len(nums)-1)
	fmt.Println(nums)
}