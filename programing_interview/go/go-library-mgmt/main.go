package main

import (
	"fmt"

	"github.com/ajaycloud9/master-python/programing_interview/go/cryptic/decrypt"
	"github.com/ajaycloud9/master-python/programing_interview/go/cryptic/encrypt"
	"github.com/pborman/uuid"
)

func main() {
	uuid := uuid.NewRandom().String()
	fmt.Println(uuid)
	encrypted_str := encrypt.Encode("Ajay Singh")
	fmt.Println(decrypt.Decode(encrypted_str))

}
