//usr/local/bin/go run $0 $@ ; exit

package main

import "fmt"

func main() {

	for i :=0.01; i <= 1; i = i + 0.01 {
    fmt.Println(i)
  }

}
