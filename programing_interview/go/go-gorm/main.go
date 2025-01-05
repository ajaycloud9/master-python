package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
	"gorm.io/driver/sqlserver"
	"gorm.io/gorm"
)

type Student struct {
	ID    uint   `json:"id" gorm:"primaryKey"`
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Email string `json:"email"`
}

var db *gorm.DB

func initDatabase() {
	var err error
	// Replace with your SQL Server connection details
	dsn := "sqlserver://username:password@localhost:1433?database=StudentDB"
	db, err = gorm.Open(sqlserver.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("Failed to connect to SQL Server!")
	}
	db.AutoMigrate(&Student{})
}

func main() {
	// Initialize database
	initDatabase()

	// Set up router
	router := mux.NewRouter()

	router.HandleFunc("/students", getStudents).Methods("GET")
	router.HandleFunc("/students/{id}", getStudentByID).Methods("GET")
	router.HandleFunc("/students", createStudent).Methods("POST")
	router.HandleFunc("/students/{id}", updateStudent).Methods("PUT")
	router.HandleFunc("/students/{id}", deleteStudent).Methods("DELETE")

	// Start server
	http.ListenAndServe(":8080", router)
}

// Handlers
func getStudents(w http.ResponseWriter, r *http.Request) {
	var students []Student
	db.Find(&students)
	json.NewEncoder(w).Encode(students)
}

func getStudentByID(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	var student Student
	if err := db.First(&student, id).Error; err != nil {
		http.Error(w, "Student not found", http.StatusNotFound)
		return
	}
	json.NewEncoder(w).Encode(student)
}

func createStudent(w http.ResponseWriter, r *http.Request) {
	var student Student
	if err := json.NewDecoder(r.Body).Decode(&student); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	db.Create(&student)
	json.NewEncoder(w).Encode(student)
}

func updateStudent(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	var student Student
	if err := db.First(&student, id).Error; err != nil {
		http.Error(w, "Student not found", http.StatusNotFound)
		return
	}

	if err := json.NewDecoder(r.Body).Decode(&student); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	db.Save(&student)
	json.NewEncoder(w).Encode(student)
}

func deleteStudent(w http.ResponseWriter, r *http.Request) {
	id := mux.Vars(r)["id"]
	var student Student
	if err := db.First(&student, id).Error; err != nil {
		http.Error(w, "Student not found", http.StatusNotFound)
		return
	}
	db.Delete(&student)
	w.WriteHeader(http.StatusNoContent)
}
