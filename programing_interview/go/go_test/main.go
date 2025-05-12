package go_test

const englishHello = "Hello, "

func Hello(name string) string {

	if name == "" {
		name = "world"
	}
	return englishHello + name
}
