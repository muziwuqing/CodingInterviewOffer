package main

import "strings"
import "fmt"

func replaceSpace(s string) string {
	return strings.Replace(s, " ", "%20", -1)
}

func main() {
	s := "we are happy"
	res := replaceSpace(s)
	fmt.Println(res)
}