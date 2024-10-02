package main

import "fmt"

func main() {
	// var colors map[string]string
	// colorss := make(map[string]string)
	colors := map[string]string{
		"red":   "#ff0000",
		"green": "$dfsfs",
		"White": "test",
	}
	fmt.Println(colors)
	iterDict(colors)
}

func iterDict(d map[string]string) {
	for key, value := range d {
		fmt.Println(key, value)
	}
}
