package main

import (
	"html/template"
	"log"
	"net/http"
	"path/filepath"
)

type User struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
}

// Handle POST request
func handlePost(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
		return
	}

	firstName := r.FormValue("first_name")
	lastName := r.FormValue("last_name")

	// Create a User instance
	user := User{
		FirstName: firstName,
		LastName:  lastName,
	}

	// Create a response template
	tmpl := `
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting</title>
    </head>
    <body>
        <h1>Hello, {{.FirstName}} {{.LastName}}!</h1>
        <p>Thank you for submitting your details.</p>
    </body>
    </html>
    `
	t := template.Must(template.New("response").Parse(tmpl))

	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	t.Execute(w, user)
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, filepath.Join("static", "index.html"))
}

func main() {
	http.HandleFunc("/", handleIndex)
	http.HandleFunc("/submit", handlePost)
	log.Fatal(http.ListenAndServe(":8081", nil))
}
