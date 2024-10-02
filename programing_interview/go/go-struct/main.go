package main

import "fmt"

type person struct {
	firstname string
	lastname  string
	contactInfo
}

type contactInfo struct {
	email string
	zip   int
}

func main() {
	alex := person{firstname: "Alex", lastname: "Anderson"}
	var shaliesh person
	fmt.Println(alex, shaliesh)
	shaliesh.firstname = "Vijay"
	shaliesh.lastname = "Singh"
	shaliesh.contactInfo.email = "sai@gmail.com"
	shaliesh.contactInfo.zip = 123
	fmt.Println(alex, shaliesh)

	shaliesh.updateName("Ajay")
	fmt.Println(alex, shaliesh)
}

func (pointertoPerson *person) updateName(newname string) {
	(*pointertoPerson).firstname = newname
}
