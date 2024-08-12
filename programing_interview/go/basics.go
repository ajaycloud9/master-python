package main
import "fmt"

func printGreeting(str string) {

	fmt.Println("Hey there,", str)
}


//High order function
func calArea(test float64) {
	fmt.Println("Ajay")
	// return test
}

func calcPerimeter(test float64) {
	fmt.Println("Vjay")
	// return test // You need to return a float64 value here
}


func getFunction(query int) func(r float64) {

	// Creating a dictionary with Key as integer
	// Value as function(args type) return type
	query_to_func := map[int]func(r float64) {
		1: calArea,
		2: calcPerimeter,
	}
	return query_to_func[query]
}
func printMyName() {
	fmt.Println("Ajay")
}

func greetings() (x, y string) {
	x = "hello "
	y = "world"
	return
}

// Pointer is a variable that holds memory address of 
// another variable

// They point where the memory is allocated and provide ways to find
// or even change the value located at the memory location

// if you  need to find the memory address of the operator
// please look for the obtained by preceding the name of a variable
// with an ampersand sign (&), known as address-of operator

// * deference operator if you put the * it will find the
// memory and the return the value it stores at that location

func my_pointer(){
	i := 10
	fmt.Println("%T %v \n", &i, &i)
	fmt.Println("%T %v \n", *(&i), *(&i))

	//Declaring the pointer
	//var <pointer_name> *<data_type>
	// var ptr_i *int
	// var ptr_s *string

 
	// var ptr_i *int = &i
	// ptr_i := &i
}

// Passing by value in fuctions
// Function is called by directly passing the value of the variable
// as an argument

// the parameter is copied into another location of your memory

// So, when accessing or modifying the variable within your function,
// only the copy is accessed or modified and the original value is
// never modified

// All basic types(int, float, bool, string,array) are passed by value

// Passing by reference
// Go supports pointers, allowing you to pass references, to values within
// your program
// In call by reference/pointer the address of the variable is passed into
// the function call as the actual parameter
// All the operations in the function are performed on the value stored at
// the address of the actual parameters

func modify_val(s string) {
	s = "world"
}

func modify_list(mylist []int){
	mylist[0] = 100
	// I am working on the same list 
	// Which is passed and, changing 
	// the real value
}

func modify_map(mymap map[string]int) {
	mymap["K"] = 25 
}

func modify_ref(s *string) {
	*s = "world"
}

// Struct

// User-defined data types
// a Structure that groups together data elements
// provide a way to reference a serices of grouped values
// through a single variable name

type Student struct {
	name string
	rollNo int
}

//Passing by reference

type Circle struct {
	x int
	y int
	radius float64
	area float64
}

// *Circle is just indicating that 
// Argument is coming as a pointer
// memory location of the struct circle
func CalArea(c *Circle) {
	const PI float64 = 3.14
	var area float64
	area = (PI * c.radius * c.radius)
	//Derefencing the pointer to get the actual
	// and set the actual value to the area
	(*c).area = area
}

// Methods
// A method augments a function by adding an extra parameter section immediately after the `func` keyword that accepts
// a single argument
// A method is a function which has a defined receiver
func (c *Circle) calAreamethod() {
	c.area = 3.14 * c.radius * c.radius
}

//Interfaces
// An interface specifies a method set and is a powerful way to introduce modularity in Go
// Interface is like a blueprint for a method set. They descirbe all the methods of a method set by providing
// the function signature for each method
// They specify a set of method, but do not implement them 
// A type implements an interface by implementing it's method
// The go lang intefaces are implemented implicity
// And, it doesn't not have any specific keyword to implement an interface
type shape interface {
	area() float64
	perimeter() float64

}

type square struct {
	side float64
}

type rect struct{
	length,breadth float64
}

func (r rect) area() float64 {
	return r.length * r.breadth
}

func (r rect) perimeter() float64 {
	return 2*r.length + 2*r.breadth
}

func (s square) area() float64 {
	return s.side * s.side
}

//reciever is struct tyoe square
// return type is float
// function signature has 3 items <reciever> name() return_type
func (s square) perimeter() float64 {
	return 4 * s.side
}

// beauty here is it is taking the whole interface as argument
// interface contains signature of all the methods
// All we are doing is printing the return values of all the methods
// User doesn't have to think what's happening inside this method
func printdata (s shape) {
	fmt.Println(s)
	fmt.Println(s.area())
	fmt.Println(s.perimeter())
}

func main() {
	// printGreeting("Joe")
	// getFunction(1)(1)
	// printMyName()
	// fmt.Print(greetings())
	// my_pointer()
	a := "hello"
	fmt.Println(a)
	//Not changing the actual value
	modify_val(a)
	fmt.Println(a)
	// Changing the actual value
	modify_ref(&a)
	fmt.Println(a)

	//Slices are passed by reference by default
	slice := []int{10,20,30}
	fmt.Println(slice)
	modify_list(slice)
	fmt.Println(slice)

	//Maps, as well are passed by reference by default
	// ascii_code := make(map[string]int)
	// ascii_code["A"] = 65
	// ascii_code["F"] = 70
	// fmt.Println(ascii_code)
	// modify_map(ascii_code)
	// fmt.Println(ascii_code)
	// //Init struct

	// st := Student{
	// 	name: "Joe",
	// 	rollNo: 12,
	// }
	// fmt.Println("%+v", st)

	// c := Circle{x:5, y:5, radius:10, area:0}
	// fmt.Println("%+v",c)
	// CalArea(&c)
	// fmt.Printf("%v \n", c)

	// c_method := Circle{radius:25}
	// c_method.calAreamethod()
	// fmt.Println("%+v", c_method)
	s := square{side:3}
	r := rect{length:7, breadth:1}
	printdata(s)
	printdata(r)
	fmt.Println("Ajay")
}
