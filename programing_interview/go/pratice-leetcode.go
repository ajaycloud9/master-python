package main
import (
    "strconv"
    "fmt"
	"reflect"
	"strings"
)

func main () {
	x := 121
	mystr := strconv.Itoa(x)
	fmt.Println("%T %v", mystr, mystr)
	fmt.Println(reflect.TypeOf(mystr))
	arrayofstring := strings.Split(mystr,"")
	fmt.Println("%T %v", arrayofstring, arrayofstring)
	for i,digit := range arrayofstring {
		fmt.Println(i,digit)
	}
	fmt.Println("=========================")
	for i:=0; i < len(arrayofstring); i++ {
		fmt.Println(i,arrayofstring[i])
	}
	fmt.Println("============REVERSE=========")
	for i:=len(arrayofstring)-1; i >= 0; i-- {
		fmt.Println(i,arrayofstring[i])
	}
}



