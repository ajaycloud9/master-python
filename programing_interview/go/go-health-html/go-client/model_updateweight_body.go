/*
 * Weight Tracker API
 *
 * API for inserting a person's weight record.
 *
 * API version: 1.0.0
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type UpdateweightBody struct {
	// Unique identifier for the person
	PersonId int32 `json:"person_id"`
	// First name of the person
	FirstName string `json:"first_name"`
	// Last name of the person
	LastName string `json:"last_name"`
	// Date of the weight record
	Date string `json:"date"`
	// Weight of the person in kg
	Weight float32 `json:"weight"`
}