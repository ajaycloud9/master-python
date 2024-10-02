package main

import (
	"os"
	"testing"
)

// t.Errorf("Expected deck length of 16, but got %v", len(d))

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 20 {
		t.Errorf("Expected deck length of 20, but got %v", len(d))

	}
	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card %v", d[0])
	}
	if d[len(d)-1] != "Five of Clubs" {
		t.Errorf("Expected last card %v", d[len(d)-1])
	}

}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	os.Remove("_decktesting")

	d := newDeck()
	d.saveToFile("_decktesting")

	loadedDec := newDeckFromFile("_decktesting")

	if len(loadedDec) != 20 {
		t.Errorf("Expected deck length of 20, but got %v", len(d))
	}
	os.Remove("_decktesting")
}
