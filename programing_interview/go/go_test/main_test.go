package main

import (
	"fmt"
	"testing"

	_ "github.com/stretchr/testify/suite"
)

// TestSuite struct to hold test state
type TestSuite struct {
	value int
}

// Setup initializes the test suite
func (suite *TestSuite) Setup() {
	suite.value = 42
	fmt.Println("Set-up")
}

// Teardown cleans up after tests
func (suite *TestSuite) Teardown() {
	suite.value = 0
	fmt.Println("Teardown")
}

// TestAdd tests the Add function
func TestAdd(t *testing.T) {
	suite := &TestSuite{}
	suite.Setup()
	defer suite.Teardown()

	result := Add(1, 2)
	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}

// TestAnother tests another case
func TestAnother(t *testing.T) {
	suite := &TestSuite{}
	suite.Setup()
	defer suite.Teardown()

	if suite.value == 42 {
		t.Errorf("Expected value to be 23, got %d", suite.value)
	}
}
