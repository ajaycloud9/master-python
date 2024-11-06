package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/prometheus/client_golang/prometheus"
	_ "github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	_ "github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	_ "github.com/prometheus/client_golang/prometheus/promhttp"
)

func main() {
	startMyApp()
}

var REQUEST_COUNT = promauto.NewCounter(prometheus.CounterOpts{
	Name: "go_app_request_count",
	Help: "Total App Http Request Count",
})

func startMyApp() {

	router := mux.NewRouter()
	router.HandleFunc("/birthday/{name}", func(rw http.ResponseWriter, r *http.Request) {

		vars := mux.Vars(r)
		name := vars["name"]
		greetings := fmt.Sprintf("Happy Birthday %s!", name)
		rw.Write([]byte(greetings))
		REQUEST_COUNT.Inc()
	}).Methods("GET")

	log.Println("Starting application server")
	router.Path("/metrics").Handler(promhttp.Handler())
	http.ListenAndServe(":8000", router)
}

// func startMyApp() {
// 	// Create a new router
// 	router := mux.NewRouter()

// 	// Define the route and handler
// 	router.HandleFunc("/birthday/{name}", func(rw http.ResponseWriter, r *http.Request) {
// 		// Extract the name from the URL parameters
// 		vars := mux.Vars(r)
// 		name := vars["name"]

// 		// Create the greeting message
// 		greetings := fmt.Sprintf("Happy Birthday %s!", name)

// 		// Write the response
// 		rw.Write([]byte(greetings))
// 	}).Methods("GET")

// 	// Log that the server is starting
// 	log.Println("Starting application server on :8000")

// 	// Start the server on port 8000
// 	http.ListenAndServe(":8000", router)
// }
