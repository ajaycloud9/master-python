package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

// Create a new type of deck
// which is a slice of strings

// deck type same as behaviour as slice of string
type deck []string

func newDeck() deck {
	cards := deck{} //Initializing the dec type
	cardSuites := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardValues := []string{"Ace", "Two", "Three", "Four", "Five"}

	for _, suit := range cardSuites {
		for _, value := range cardValues {

			cards = append(cards, value+" of "+suit)
		}
	}
	return cards
}

// Function receives the argument
func deal(d deck, handsize int) (deck, deck) {
	return d[:handsize], d[handsize:]
}

// Recevier as deck
func (d deck) print() {
	for i, car := range d {
		fmt.Println(i, car)
	}
}

func (d deck) toString() string {
	return strings.Join(d, ",")

}

func (d deck) saveToFile(filename string) error {
	return os.WriteFile(filename, []byte(d.toString()), 0666)
}

func newDeckFromFile(filename string) deck {
	bs, err := os.ReadFile(filename)
	if err != nil {
		// Option #1 - Log the error and return a call to newDeck()
		// Option #2 - Log error and Exit the program
		fmt.Println("Error: ", err)
		os.Exit(1)
	}
	ss := strings.Split(string(bs), ",")
	return deck(ss)
}

func (d deck) shuffle() {
	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)
	for index, _ := range d {
		rand_value := r.Intn(len(d) - 1)
		d[index], d[rand_value] = d[rand_value], d[index]
	}
}
