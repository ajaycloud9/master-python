package main

import "fmt"

// Interface is solving the problem of
// Not re-interatting the calling of the same function
// for different types and, once function common for all
// the types can be used at once
type bot interface {
	getGreeting() string
}
type englishbot struct{}
type spanishhbot struct{}

// Greeting of type english bot
// Class English.greeting() return hello
func (eb englishbot) getGreeting() string {
	return "Hi there"
}

// Class Spanish.greeting() return Holla!
// This is like a class function
func (sb spanishhbot) getGreeting() string {
	return "Hola!"
}

// printGreeting is like a independent function
// Hence, printgreetings can't be duplicated

// func printGreeting(eb englishbot) {
// 	fmt.Println(eb.getGreeting())
// }

// func printGreeting(sb spanishhbot) {
// 	fmt.Println(sb.getGreeting())
// }

// We can use a interface which is now
// taking greetfunction not especfic to any class
// Any of the class or type object can share that
// Common interface hence, greeeting function is
// defined with arguments and with return type
func printGreeting(b bot) {
	fmt.Println(b.getGreeting())
}

func main() {

	// Declared both the objects or types
	eb := englishbot{}
	sb := spanishhbot{}

	// Now calling print function which
	// Can eventually call all other similar
	// type of greet function from different
	// language of chatbots
	printGreeting(eb)
	printGreeting(sb)
}
