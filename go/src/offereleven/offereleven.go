package main

import "fmt"

func minArray(numbers []int) int {
	l, r := 0, len(numbers) - 1
	for l < r {
		mid := (l + (r - 1)) >> 1
		if numbers[mid] > numbers[r] {
			l = mid + 1
		} else if numbers[mid] < numbers[l] {
			r = mid
		} else {
			r--
		}
	}
	return numbers[l]
}		

func main() {
	numbers := []int{4, 5, 1, 2, 3}
	fmt.Println(minArray(numbers))
}