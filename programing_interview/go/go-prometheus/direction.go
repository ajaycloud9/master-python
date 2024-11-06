package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Define the new metric with the name `distance_covered` and `direction` label
var (
	distanceCovered = prometheus.NewCounterVec(
		prometheus.CounterOpts{
			Name: "distance_covered", // Metric name
			Help: "Total distance covered in different directions.",
		},
		[]string{"direction"}, // Label for direction
	)
)

// init function to register metrics
func init() {
	// Register the metric with Prometheus
	prometheus.MustRegister(distanceCovered)

	// Log that metrics are registered
	fmt.Println("Prometheus metric 'distance_covered' registered.")
}

func randomDistance() int {
	//Randomly return a distance between 1 and 10
	return rand.Intn(10) + 1
}

func simulateMovement() {
	// Choosing a random direction and adding distance to it

	//List of strings containing directions
	directions := []string{"north", "south", "east", "west"}

	for {
		// Chose a random direction
		direction := directions[rand.Intn(len(directions))]
		distance := randomDistance()

		// Add the random distance to the appropriate direction

		distanceCovered.WithLabelValues(direction).Add(float64(distance))

		//sleep for 20 secs before simulating the next movement
		time.Sleep(30 * time.Second)
	}

}

func main() {

	// Start the simulation movement
	go simulateMovement()

	//Set up the HTTP handler to expose prometheus metrics
	http.Handle("/metrics", promhttp.Handler())

	//Start the HTTP server to serve the metrics

	fmt.Println("Starting metric server")
	http.ListenAndServe(":8000", nil)
}
