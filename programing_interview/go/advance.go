//Seqential programming 

// Go routines
// Consider aas a lightweight thread that has a seperate 
// independent execution

// Can execute concurrently with other go-routines

package main

import (
	"fmt"
	"time"
	"sync"
)


// Go rountines are independent of themselves no parent child relations ship it 
// can run freely and have no dependencies on other go rountines

// Anonymous go-routine
// In Golang, anonymous functions are those functions that don't have any name
// Simply put, anonymous functions don't use any variables as a name when they 
// are declared

// Go-routine
// Consider as a lightweight application level thread that has a seperate independent 
// Execition

// The go runtime has it's own scheduler that will multiplex the go-routines on the OS level
// threads in the go routine

// It schedules an arbitrary number of go rountines onto an arbitrary number of OS threads
// (m:n multiplexing)

// Cooperative Schedular
// Golang schedular is a cooperative schedular
// Cooperative scheduling is a style of scheduling in which the OS never interrupts a running
// Process to initiate a context switch from one process to another
// Process must voluntarily yeild control periodically or when logically blocked on a resource
// Of course, there are some specific check points where go rountine can yeild execition to other
// go-routine. These are called context switches

//Wait Groups
func calculateSquare(i int, wg *sync.WaitGroup) {
	time.Sleep(1 * time.Second)
	fmt.Println(i*i)
	wg.Done()
}


func main() {

	var wg sync.WaitGroup
	start := time.Now()
	wg.Add(10000)
	for i:=1; i <=10000; i++ {
		go calculateSquare(i, &wg)
	}
	elapsed := time.Since(start)
	// time.Sleep(2 * time.Second)
	wg.Wait()
	fmt.Println("Function took", elapsed)
}
