package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {

	resp, err := http.Get("http://google.com")

	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// //Initiating an empty byte slice
	// bs := make([]byte, 9999)
	// // Expecting Read function to fetch the raw data
	// // Fill the empty byte slice
	// resp.Body.Read(bs)
	// fmt.Println(string(bs))

	io.Copy(os.Stdout, resp.Body)

}
