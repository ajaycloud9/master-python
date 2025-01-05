package main

func newCard() string {
	return "Five of diamonds"
}

func main() {

	cards := newDeck()
	// fmt.Println(cards.toString())
	cards.saveToFile("my_cards.txt")
	// new_cards := newDeckFromFile("my_cards.txt")
	cards.shuffle()
	cards.print()
	// cards.print()
	// hand, remainCard := deal(cards, 5)
	// hand.print()
	// remainCard.print()
}
