package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"path/filepath"

	"github.com/bxcodec/faker/v3"
)

type Tag struct {
	Name         string `json:"name"`
	Type         string `json:"type" faker:"oneof:auto, manual, policy"`
	ServiceOwner string `json:"serviceOwner" faker:"oneof:edge, network, iam"`
	OwnerID      int    `json:"ownerId"`
	Access       string `json:"access" faker:"oneof:read, write"`
	Description  string `json:"description" faker:"sentence"`
	Parent       string `json:"parent" faker:"uuid_digit"`
}

func main() {
	dir := "/Users/ajaysingh/tag_creation_json_files"
	err := os.MkdirAll(dir, os.ModePerm)
	if err != nil {
		log.Fatalf("Failed to create directory: %v", err)
	}

	var fileNames []string

	for ownerID := 1; ownerID <= 50; ownerID++ {
		var tags []Tag

		for tagID := 1; tagID <= 10; tagID++ {
			tag := Tag{}
			err := faker.FakeData(&tag)
			if err != nil {
				log.Fatalf("Error generating fake data: %v", err)
			}

			tag.OwnerID = ownerID
			tag.Name = fmt.Sprintf("owner-%d-tag-%d", ownerID, tagID) // Set the Name field with the desired pattern

			tags = append(tags, tag)
			fmt.Println(tags)
		}

		jsonData, err := json.MarshalIndent(tags, "", "  ")
		if err != nil {
			log.Fatalf("Error marshalling JSON: %v", err)
		}

		fileName := filepath.Join(dir, fmt.Sprintf("tag_creation_%02d.json", ownerID))
		tempFileName := fmt.Sprintf("tag_creation_%02d.json", ownerID)
		err = os.WriteFile(fileName, jsonData, 0644)
		if err != nil {
			log.Fatalf("Error writing to file: %v", err)
		}
		fileNames = append(fileNames, tempFileName[:len(tempFileName)-5])

	}
	// Create CSV file
	csvFilePath := filepath.Join(dir, "tag_creation_listing.csv")
	csvFile, err := os.Create(csvFilePath)
	if err != nil {
		log.Fatalf("Failed to create CSV file: %v", err)
	}
	defer csvFile.Close()

	writer := csv.NewWriter(csvFile)
	defer writer.Flush()

	// writer.Write([]string{"File Name"}) // Write header
	for _, name := range fileNames {
		writer.Write([]string{name})
	}

	fmt.Println("Successfully created 50 JSON files with 50 tags each.")
}
