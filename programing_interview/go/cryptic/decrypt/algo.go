package decrypt

func Decode(str string) string {

	decyptedStr := ""

	for _, c := range str {
		asciicode := int(c)
		new_c := string(asciicode - 3)
		decyptedStr += new_c
	}
	return decyptedStr
}
