### Go library Mgmt

Go Modules: Contains multiple packages with version
   |
   |
   - - - > package
   - - - > package
   - - - > package
             |
            v1.0.0
- Go code is grouped into packages, and packages are grouped into modules
- A module specifies the dependencies needed to run our code, including
  the Go version and the set of other module it requires in the go.mod
  file

** Name Convention of the Go Packages

- Package names should be descriptive
- Avoid repeating the name of the package in the names of functions and types
  within the package
- Every go file in a directoru must have an identical package clause
- As a rule, you should make the name of the package match the 
  name of the directory that contains the package.