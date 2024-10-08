package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"html/template"
	"log"
	"net/http"
	"os"

	_ "github.com/go-sql-driver/mysql"
)

type Person struct {
	PersonID         int
	FirstName        string
	LastName         string
	Date             string
	Weight           float64
	Date2            string
	Weight2          float64
	WeightDifference float64
}

// Person represents a person in the database
type PersonJson struct {
	PersonID  int     `json:"person_id"`
	FirstName string  `json:"first_name"`
	LastName  string  `json:"last_name"`
	Date      string  `json:"date"`
	Weight    float64 `json:"weight"`
}

// Function to read SQL query from a file
func readSQLFile(filename string) (string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return "", err
	}
	return string(data), nil
}

func getAllPersons(db *sql.DB, query string) ([]Person, error) {

	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var persons []Person

	for rows.Next() {
		var p Person
		// Here, you need to adjust the Scan method to match all columns selected.
		if err := rows.Scan(&p.PersonID, &p.FirstName, &p.LastName, &p.Date, &p.Weight); err != nil {
			return nil, err
		}
		persons = append(persons, p)
	}
	fmt.Println(persons)
	return persons, nil
}

// Function to run the weight difference query
func getWeightDifferences(db *sql.DB, query string) ([]Person, error) {
	// Execute the query
	rows, err := db.Query(query)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	var persons []Person
	// Process the results
	fmt.Println("Results:")
	for rows.Next() {
		var p Person
		if err := rows.Scan(&p.PersonID, &p.FirstName, &p.LastName, &p.Date, &p.Weight, &p.Date2, &p.Weight2, &p.WeightDifference); err != nil {
			return nil, err
		}
		persons = append(persons, p)
	}
	return persons, nil
}

// Placeholder for the getAllPersons function
func getAllPersonsJson(db *sql.DB) ([]PersonJson, error) {
	// Implement your logic to retrieve all persons from the database
	return []PersonJson{}, nil
}

// InsertPersonRecord inserts a person record into the database
func InsertPersonRecord(db *sql.DB, person PersonJson) error {
	query := `INSERT INTO Person (person_id, first_name, last_name, date, weight) VALUES (?, ?, ?, ?, ?)`
	_, err := db.Exec(query, person.PersonID, person.FirstName, person.LastName, person.Date, person.Weight)
	return err
}

func DeleteRecord(db *sql.DB, person PersonJson) error {
	query := `DELETE FROM Person WHERE first_name = ? AND last_name = ? AND date = ?`
	_, err := db.Exec(query, person.FirstName, person.LastName, person.Date)
	return err
}

func viewPersons(db *sql.DB) {
	query := "SELECT person_id, first_name, last_name, date, weight FROM Person"
	rows, err := db.Query(query)
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	// Print the results
	fmt.Println("Person Records:")
	for rows.Next() {
		var personID int
		var firstName, lastName string
		var date string
		var weight float64

		// Scan the row into variables
		if err := rows.Scan(&personID, &firstName, &lastName, &date, &weight); err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%d: %s %s, Date: %s, Weight: %.2f\n", personID, firstName, lastName, date, weight)
	}

	// Check for errors from iterating over rows
	if err := rows.Err(); err != nil {
		log.Fatal(err)
	}
}

func handleRequests(db *sql.DB) {
	query1 := `
		SELECT *
		FROM Person
		ORDER BY date, weight DESC;`
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		persons, err := getAllPersons(db, query1)
		if err != nil {
			http.Error(w, "Error retrieving data", http.StatusInternalServerError)
			return
		}

		tmpl, err := template.ParseFiles("complete_person_table.html")
		if err != nil {
			http.Error(w, "Error loading template", http.StatusInternalServerError)
			return
		}

		if err := tmpl.Execute(w, persons); err != nil {
			http.Error(w, "Error executing template", http.StatusInternalServerError)
		}
	})

	query, err := readSQLFile("weight_diff.sql")
	if err != nil {
		log.Fatal(err)
	}
	http.HandleFunc("/leaderboard", func(w http.ResponseWriter, r *http.Request) {
		persons, err := getWeightDifferences(db, query)
		if err != nil {
			http.Error(w, "Error retrieving data", http.StatusInternalServerError)
			return
		}

		tmpl, err := template.ParseFiles("template.html")
		if err != nil {
			http.Error(w, "Error loading template", http.StatusInternalServerError)
			return
		}

		if err := tmpl.Execute(w, persons); err != nil {
			http.Error(w, "Error executing template", http.StatusInternalServerError)
		}
	})

	http.HandleFunc("/updateweight", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
			return
		}

		var person PersonJson
		if err := json.NewDecoder(r.Body).Decode(&person); err != nil {
			http.Error(w, "Invalid input", http.StatusBadRequest)
			return
		}
		if err := InsertPersonRecord(db, person); err != nil {
			http.Error(w, "Error inserting person", http.StatusInternalServerError)
			return
		}
		// Respond with a success message
		w.WriteHeader(http.StatusCreated)
		json.NewEncoder(w).Encode(map[string]string{"message": "Person added successfully"})

	})

	http.HandleFunc("/deleteweight", func(w http.ResponseWriter, r *http.Request) {

		// If this is not delete request return Method not allowed
		if r.Method != http.MethodDelete {
			http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
			return
		}

		var person PersonJson
		if err := json.NewDecoder(r.Body).Decode(&person); err != nil {
			http.Error(w, "Invalid input", http.StatusBadRequest)
			return
		}
		if err := DeleteRecord(db, person); err != nil {
			http.Error(w, "Error inserting person", http.StatusInternalServerError)
			return
		}
		// Respond with a success message
		w.WriteHeader(http.StatusOK)
		json.NewEncoder(w).Encode(map[string]string{"message": "Person deleted successfully"})

	})

}

func main() {
	// Change the user, password, dbname, and other parameters as needed
	dsn := "root:dangerous@tcp(localhost:3306)/inventory"
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Check if the connection is successful
	if err := db.Ping(); err != nil {
		log.Fatal(err)
	}
	fmt.Println("Database connection established!")
	// viewPersons(db)
	// Read the SQL query from the file
	// query, err := readSQLFile("weight_diff.sql")
	if err != nil {
		log.Fatal(err)
	}

	// Call the function to get weight differences
	// getWeightDifferences(db, query)

	viewPersons(db)
	handleRequests(db)
	// query := `
	//     SELECT *
	//     FROM Person;`
	// getAllPersons(db, query)

	fmt.Println("Server starting on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))

}
