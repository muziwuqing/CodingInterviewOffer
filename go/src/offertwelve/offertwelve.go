package main

import "fmt"

func exist(board [][]byte, word string) bool {
	if len(board) == 0 {
		return false
	}
	isVisited := make([][]bool, len(board))
	for i := 0; i<len(board); i++ {
		isVisited[i] = make([]bool, len(board[0]))
	}
	for i := 0; i<len(board); i++ {
		for j :=0; j<len(board[0]); j++{
			if board[i][j] == word[0] {
				if bfs(board, word, 0, i, j, isVisited){
					return true
				}
			}
		}
	}
	return false
}

func bfs(board [][]byte, word string, cur int, i int, j int, isVisited [][]bool) bool {
	if cur == len(word) {
		return true
	}
	if i < 0 || j < 0 || i == len(board) || j == len(board[0]) || isVisited[i][j] || board[i][j] != word[cur] {
		return false
	}
	isVisited[i][j] = true
	res := bfs(board, word, cur+1, i+1, j, isVisited) ||
		bfs(board, word, cur+1, i, j+1, isVisited) ||
		bfs(board, word, cur+1, i-1, j, isVisited) ||
		bfs(board, word, cur+1, i, j-1, isVisited)
	isVisited[i][j] = false
	return res
}

func main() {
	board := [][]byte{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}
	word := "ABCCED"
	res := exist(board, word)
	fmt.Println(res)
}