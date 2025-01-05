package encrypt

func Encode(str string) string {

	encrytedStr := ""

	for _, c := range str {
		asciicode := int(c)
		new_c := string(asciicode + 3)
		encrytedStr += new_c
	}
	return encrytedStr
}
