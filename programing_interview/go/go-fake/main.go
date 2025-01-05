package main

import (
	generator "go-fake/testdatagenerator"
)

func main() {
	tagDataList := generator.CreateTagDataSet("tag_creation_json_files", "tag_creation_listing.csv", 10, 50)
	generator.DeleteTagDataSet("tag_deletion_json_files", "tag_deletion-listing.csv", tagDataList)
}
