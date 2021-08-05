package main

import "fmt"

func movingCount(m int, n int, k int) int {
    visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}
	return dfs(m, n, k, visited, 0, 0)
}

func getDigitSum(num int) int {
	sum := 0
	for num > 0 {
		sum += num %10
		num /= 10
	}
	return sum
}

func dfs(m int, n int, k int, visited [][]bool, i int, j int) int {
	res := 0
	if 0 <= i && i < m && 0 <= j && j < n && !visited[i][j] && getDigitSum(i) + getDigitSum(j) <= k {
		visited[i][j] = true
		res = 1 + dfs(m, n, k, visited, i+1, j) + dfs(m, n, k, visited, i, j+1)
	}
	return res
}

func main() {
	m, n , k := 3, 2 ,17
	res := movingCount(m, n, k)
	fmt.Println(res)
}