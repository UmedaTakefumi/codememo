//usr/local/bin/go run $0 $@ ; exit

package main

import (
	"fmt"
//	"reflect"
)

func main() {

  int_loop()
}

func int_loop(){

  a :=1
  //fmt.Println("Type of a")
  //fmt.Println(reflect.TypeOf(a))

  for a <= 100 {
    fmt.Printf("%v\n", a)
    a = a + 1
  }

}

