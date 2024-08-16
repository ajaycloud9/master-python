package main

import (
	"fmt"

	"github.com/ajaycloud9/master-python/cryptic/decrypt"
	"github.com/ajaycloud9/master-python/cryptic/encrypt"
)

func main() {
	encrypted_str := encrypt.Encode("Ajay Singh")
	fmt.Println("Encrypted str:- ", encrypted_str)
	fmt.Println("Decrypted str:- ", decrypt.Decode(encrypted_str))
}
