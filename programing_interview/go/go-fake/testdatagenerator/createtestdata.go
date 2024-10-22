package testdatagenerator

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

type TagData struct {
	OwnerID  int      `json:"ownerId"`
	TagNames []string `json:"tagNames"`
}

func CreateTagDataSet(dir string, csvfilename string, owners int, tagsperowner int) []TagData {
	err := os.MkdirAll(dir, os.ModePerm)
	if err != nil {
		log.Fatalf("Failed to create directory: %v", err)
	}

	var fileNames []string
	var tagDataList []TagData

	for ownerID := 1; ownerID <= owners; ownerID++ {
		var tags []Tag
		var tagNames []string

		for tagID := 1; tagID <= tagsperowner; tagID++ {
			tag := Tag{}
			err := faker.FakeData(&tag)
			if err != nil {
				log.Fatalf("Error generating fake data: %v", err)
			}

			tag.OwnerID = ownerID
			tag.Name = fmt.Sprintf("owner-%d-tag-%d", ownerID, tagID) // Set the Name field with the desired pattern

			tags = append(tags, tag)
			tagNames = append(tagNames, tag.Name)
			// fmt.Println(tags)
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

		// Add to tagDataList
		tagDataList = append(tagDataList, TagData{
			OwnerID:  ownerID,
			TagNames: tagNames,
		})
	}
	// Create CSV file
	csvFilePath := filepath.Join(dir, csvfilename)
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

	fmt.Sprintf("Successfully created %v JSON files with %v tags each.", owners, tagsperowner)
	return tagDataList
}

func DeleteTagDataSet(dir string, csvfilename string, t []TagData) {
	var fileNames []string
	err := os.MkdirAll(dir, os.ModePerm)
	if err != nil {
		log.Fatalf("Failed to create directory: %v", err)
	}

	for id, data := range t {
		jsonData, err := json.MarshalIndent(data, "", "  ")
		if err != nil {
			log.Fatalf("Error marshalling JSON: %v", err)
		}
		fileName := filepath.Join(dir, fmt.Sprintf("tag_deletion_%02d.json", id+1))
		tempFileName := fmt.Sprintf("tag_deletion_%02d.json", id+1)
		fileNames = append(fileNames, tempFileName[:len(tempFileName)-5])
		err = os.WriteFile(fileName, jsonData, 0644)
		if err != nil {
			log.Fatalf("Error marshalling JSON: %v", err)
		}
		// fmt.Println(string(jsonData))
		// Create CSV file
		csvFilePath := filepath.Join(dir, csvfilename)
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
	}
}
